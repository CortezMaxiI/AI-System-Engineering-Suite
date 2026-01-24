import os
import datetime
from typing import Any

try:
    from supabase import create_client, Client
except ImportError:
    Client = Any
    create_client = None

class SupabaseLogger:
    def __init__(self):
        self.url = os.getenv("SUPABASE_URL")
        self.key = os.getenv("SUPABASE_KEY")
        self.client: Client = None
        self.enabled = False

        self._initialize_client()

    def _initialize_client(self):
        if not create_client:
            print(f"[\033[93mWARN\033[0m] 'supabase' library not installed. Persistence disabled.")
            return

        if self.url and self.key:
            try:
                self.client = create_client(self.url, self.key)
                self.enabled = True
                print(f"[\033[96mDB\033[0m] Supabase Client Connected.")
            except Exception as e:
                print(f"[\033[91mERR\033[0m] Supabase connection failed: {e}")
                self.enabled = False
        else:
            print(f"[\033[93mWARN\033[0m] Missing SUPABASE_URL or SUPABASE_KEY. Persistence disabled.")

    def log_decision(self, symbol: str, price: float, signal: str, confidence: float, reasoning: str):
        """
        Logs a trading decision to Supabase.
        Fails safe (does not raise exception) if DB is unreachable.
        """
        if not self.enabled or not self.client:
            return

        try:
            data = {
                "timestamp": datetime.datetime.utcnow().isoformat(),
                "symbol": symbol,
                "price": float(price), # Ensure numeric
                "signal": signal,
                "confidence": float(confidence), # Ensure numeric
                "reasoning": reasoning
            }

            # Execute insert
            self.client.table("trade_logs").insert(data).execute()
            
            # log success
            print(f"[\033[96mDB\033[0m] Saved")

        except Exception as e:
            # Resilience: Catch connection errors, timeouts, auth errors, etc.
            # Do NOT crash the bot.
            print(f"[\033[91mERR\033[0m] Failed to save to DB: {e}")
