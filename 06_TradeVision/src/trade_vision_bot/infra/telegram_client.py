import os
import requests
from typing import Optional

class TelegramClient:
    def __init__(self):
        self.token = os.getenv("TELEGRAM_TOKEN")
        self.chat_id = os.getenv("TELEGRAM_CHAT_ID")
        self.enabled = bool(self.token and self.chat_id)
        
        if self.enabled:
            print(f"[\033[94mINFO\033[0m] Telegram Voice Engine Connected.")
        else:
            print(f"[\033[93mWARN\033[0m] Telegram credentials missing. Voice Engine disabled.")

    def send_alert(self, formatted_message: str):
        """
        Sends a pre-formatted alert to Telegram.
        """
        if not self.enabled:
            return

        try:
            url = f"https://api.telegram.org/bot{self.token}/sendMessage"
            payload = {
                "chat_id": self.chat_id,
                "text": formatted_message,
                "parse_mode": "Markdown"
            }
            
            response = requests.post(url, json=payload, timeout=10)
            
            if response.status_code == 200:
                print(f"[\033[94mTG\033[0m] Alert sent successfully.")
            else:
                print(f"[\033[91mERR\033[0m] Telegram API Error: {response.text}")

        except Exception as e:
            # Resilience: Fail silently (log to console but don't stop the bot)
            print(f"[\033[91mERR\033[0m] Failed to reach Telegram: {e}")
