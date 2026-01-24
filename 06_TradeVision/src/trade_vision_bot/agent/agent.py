import time
import os
import requests
from strategies.technical_strategy import TechnicalStrategy
from infra.supabase_client import SupabaseLogger
from infra.telegram_client import TelegramClient

class TradeAnalystAgent:
    def __init__(self):
        print("[\033[92mAGENT\033[0m] TradeVision Analyst v2.1 (News Intelligence Active)")
        
        # Tools
        self.strategy = TechnicalStrategy() 
        self.memory = SupabaseLogger()
        self.voice = TelegramClient()
        
        # News Intelligence Check
        self.panic_token = os.getenv("CRYPTOPANIC_TOKEN")
        if not self.panic_token:
            print("[\033[91mERR\033[0m] CRYPTOPANIC_TOKEN not found in .env. Sentiment Engine failed.")
        else:
            print("[\033[94mSENTIMENT\033[0m] CryptoPanic API Connected (Real-time News)")

        # State
        self.last_decision_time = 0
        self.decision_interval = 300.0 # 5 Minutes cooldown

    def fetch_market_sentiment(self):
        """
        Capa 2 (IA/Sentimiento): Fetches and analyzes news from CryptoPanic.
        Returns a score (int) and the most relevant headline.
        """
        if not self.panic_token:
            return 0.0, "Sentiment Engine Offline (Missing Token)"
        
        try:
            url = f"https://cryptopanic.com/api/v1/posts/?auth_token={self.panic_token}&kind=news"
            response = requests.get(url, timeout=10)
            if response.status_code != 200:
                return 0.0, "API Connection Error"
            
            data = response.json()
            posts = data.get('results', [])[:10] # Last 10 posts
            
            pos_words = ['etf', 'growth', 'support', 'accumulation', 'bullish', 'adoption', 'sec approval', 'pumping', 'positive']
            neg_words = ['lawsuit', 'hack', 'fed', 'resistance', 'dump', 'bearish', 'scam', 'crash', 'regulation', 'fud', 'negative']
            
            score = 0.0
            best_headline = "No relevant news found"
            found_relevant = False
            
            for post in posts:
                title = post.get('title', '').lower()
                p_hits = sum(1 for w in pos_words if w in title)
                n_hits = sum(1 for w in neg_words if w in title)
                
                # Heuristic: +1 point if title is overall positive, -1 if negative
                if p_hits > n_hits: score += 1
                elif n_hits > p_hits: score -= 1
                
                # Capture the first significant headline found
                if (p_hits + n_hits) > 0 and not found_relevant:
                    best_headline = post.get('title')
                    found_relevant = True
                    
            return score, best_headline

        except Exception as e:
            return 0.0, f"Fetch Error: {str(e)}"

    def process_tick(self, market_data: dict):
        """
        Main Agentic Loop for a single Tick.
        Architecture: Layers (Technical -> Sentiment Filter -> Message Gen)
        """
        try:
            # 1. Parse Data
            symbol = market_data.get('s', 'UNKNOWN')
            price = float(market_data.get('p', '0'))
            
            # 2. Update Technical State (Layer 1)
            self.strategy.update(price)
            tech_analysis = self.strategy.evaluate()
            
            # 3. Filter for initialization
            if tech_analysis["signal"] == "WAIT":
                return

            # 4. Cooldown
            now = time.time()
            if now - self.last_decision_time < self.decision_interval:
                return
            
            self.last_decision_time = now

            # 5. Layer 2: Real News Sentiment Analysis
            sentiment_score, headline = self.fetch_market_sentiment()

            # Consensus & Risk Evaluation
            final_signal = tech_analysis["signal"]
            confidence = 0.75
            risk_level = "MODERADO"
            
            # LOGIC: Filter BUYS via Sentiment
            if final_signal == "BUY":
                if sentiment_score < -0.5: # Negative bias in news
                    final_signal = "HOLD"
                    risk_level = "ALTO (Bloqueo por Noticias)"
                    confidence = 0.0
                elif sentiment_score > 0.5: # Positive bias
                    risk_level = "BAJO"
                    confidence = 0.95
            
            elif final_signal == "SELL":
                # Sell confidence increases if sentiment is also negative
                if sentiment_score < -0.5:
                    risk_level = "BAJO"
                    confidence = 0.90
                else:
                    risk_level = "MODERADO"
                    confidence = 0.70

            # 6. Act (Execute & Notify)
            if final_signal != "HOLD":
                 self._execute_decision(symbol, price, final_signal, confidence, tech_analysis, sentiment_score, headline, risk_level)

        except Exception as e:
            print(f"[\033[91mERR\033[0m] Agent Brain Fault: {e}")

    def _execute_decision(self, symbol, price, signal, confidence, tech_data, sent_score, headline, risk):
        # Console Output
        color = "\033[92m" if signal == "BUY" else "\033[91m"
        print(f"[\033[92mDECISION\033[0m] {symbol} @ {price}: {color}{signal}\033[0m [Sent:{sent_score}] [Risk:{risk}]")

        # Persistence (Supabase)
        full_reasoning = f"Tech: {tech_data['trend']} (RSI {tech_data['rsi']:.1f}) | News Score: {sent_score} | Headline: {headline}"
        self.memory.log_decision(symbol, price, signal, confidence, full_reasoning)

        # Telegram Alert (Structured Spanish)
        sent_label = "Positivo" if sent_score > 0 else "Negativo" if sent_score < 0 else "Neutral"
        msg = (
            f"🚀 *TradeVision Alert*\n\n"
            f"📊 *Datos Técnicos:*\n"
            f"• RSI: {tech_data['rsi']:.1f}\n"
            f"• Tendencia: {tech_data['trend']}\n\n"
            f"🧠 *Filtro de IA:*\n"
            f"• Sentimiento: {sent_label} ({sent_score})\n"
            f"• Riesgo: {risk}\n"
            f"• Noticia clave: {headline}\n\n"
            f"✅ *Decisión Final:*\n"
            f"• Acción: {signal} ({confidence*100:.0f}%)"
        )
        self.voice.send_alert(msg)
