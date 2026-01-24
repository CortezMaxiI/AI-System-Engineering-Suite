from collections import deque
import statistics

class TechnicalStrategy:
    def __init__(self):
        self.prices = deque(maxlen=200) # Need 200 for EMA200
        self.ema_20 = None
        self.ema_200 = None
        self.rsi_14 = None
        self.gains = deque(maxlen=14)
        self.losses = deque(maxlen=14)
        self.last_price = None

    def update(self, price: float):
        self.prices.append(price)
        
        # Calculate RSI
        if self.last_price is not None:
            delta = price - self.last_price
            if delta > 0:
                self.gains.append(delta)
                self.losses.append(0)
            else:
                self.gains.append(0)
                self.losses.append(abs(delta))
        
        self.last_price = price
        
        # Calculate EMAs
        self.ema_20 = self._calculate_ema(price, 20, self.ema_20)
        self.ema_200 = self._calculate_ema(price, 200, self.ema_200)

    def _calculate_ema(self, price, period, current_ema):
        if len(self.prices) < period:
            return None
        if current_ema is None:
            # Initialize with SMA
            return sum(list(self.prices)[-period:]) / period
        
        k = 2 / (period + 1)
        return (price * k) + (current_ema * (1 - k))

    def get_rsi(self):
        if len(self.gains) < 14:
            return 50 # Neutral default
        
        avg_gain = sum(self.gains) / 14
        avg_loss = sum(self.losses) / 14
        
        if avg_loss == 0:
            return 100
        
        rs = avg_gain / avg_loss
        return 100 - (100 / (1 + rs))

    def evaluate(self) -> dict:
        if len(self.prices) < 200:
             return {"signal": "WAIT", "rsi": 0, "trend": "Initializing"}

        rsi = self.get_rsi()
        trend = "NEUTRAL"
        
        # Determine Trend via EMA
        if self.ema_20 > self.ema_200:
            trend = "BULLISH"
        elif self.ema_20 < self.ema_200:
            trend = "BEARISH"

        # Signal Logic with RSI Confluence
        signal = "HOLD"
        
        # Buy: Bullish Trend + RSI oversold (<30) -> Reversal or strong dip buy? 
        # Or Trend Following: Bullish + RSI healthy (40-70).
        # Let's use Trend Following for this example as it's safer.
        if trend == "BULLISH" and 40 < rsi < 70:
            signal = "BUY"
        elif trend == "BEARISH" and 30 < rsi < 60: # Selling in logic
            signal = "SELL"
        
        # Overbought/Oversold Reversals (Counter-trend)
        if rsi > 70:
            signal = "SELL" # Too hot
        elif rsi < 30:
            signal = "BUY" # Oversold bounce

        return {
            "signal": signal,
            "rsi": rsi,
            "trend": trend,
            "ema_20": self.ema_20,
            "ema_200": self.ema_200
        }
