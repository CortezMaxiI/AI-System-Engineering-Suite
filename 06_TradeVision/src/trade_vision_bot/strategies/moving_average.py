from collections import deque
import statistics

class MovingAverageStrategy:
    def __init__(self, short_window=10, long_window=50):
        self.short_window = short_window
        self.long_window = long_window
        self.short_ma_buffer = deque(maxlen=short_window)
        self.long_ma_buffer = deque(maxlen=long_window)
        
        self.initialized = False

    def update(self, price: float):
        self.short_ma_buffer.append(price)
        self.long_ma_buffer.append(price)
        
        if len(self.long_ma_buffer) == self.long_window:
            self.initialized = True

    def evaluate(self) -> dict:
        if not self.initialized:
            return {"signal": "WAIT", "reason": "Gathering data..."}

        short_avg = statistics.mean(self.short_ma_buffer)
        long_avg = statistics.mean(self.long_ma_buffer)

        # Simple crossover logic
        # Ideally we'd compare with previous tick to detect the *moment* of crossover, 
        # but for this agentic loop we'll just report the current state.
        
        trend = "BULLISH" if short_avg > long_avg else "BEARISH"
        strength = abs(short_avg - long_avg)

        # Generate signal
        # A simple state-based signal, usually you want logic for entry/exit.
        # Here: If Short > Long -> BUY Zone. If Short < Long -> SELL Zone.
        
        signal = "BUY" if short_avg > long_avg else "SELL"
        
        return {
            "signal": signal,
            "short_ma": short_avg,
            "long_ma": long_avg,
            "trend": trend,
            "diff": strength
        }
