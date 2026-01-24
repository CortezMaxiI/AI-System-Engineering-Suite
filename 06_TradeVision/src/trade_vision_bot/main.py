import sys
import os
import signal
import time
from dotenv import load_dotenv
load_dotenv()


# Ensure src is in path so we can import modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from core.connector import ZMQSubscriber
from agent.agent import TradeAnalystAgent

def main():
    print("==========================================")
    print("   OPTIMAX TRADEVISION - AGENTIC CORE     ")
    print("==========================================")
    
    # 1. Initialize Agent
    bot = TradeAnalystAgent()
    
    # 2. Callback for Network Events
    stats = {"count": 0}

    def on_data(data):
        # Heartbeat: Show basic flow every 20 messages
        if 'e' in data and data['e'] == 'trade':
            stats["count"] += 1
            if stats["count"] >= 20:
                symbol = data.get('s', 'BTCUSDT')
                price = data.get('p', '0')
                # Minimalist dim log
                print(f"\033[90m[RAW] {symbol} @ {price} | Listening...\033[0m")
                stats["count"] = 0
            
            bot.process_tick(data)
        elif 'e' in data:
            pass

    # 3. Initialize Network Connector
    connector = ZMQSubscriber(topic="trade", host="tcp://127.0.0.1:5555")
    
    # 4. Handle Shutdown
    def signal_handler(sig, frame):
        print("\n[\033[93mSYS\033[0m] Shutdown signal received. Closing Eyes...")
        connector.running = False
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    # 5. Start Loop
    # This blocks until interrupted
    connector.start(callback=on_data)

if __name__ == "__main__":
    main()
