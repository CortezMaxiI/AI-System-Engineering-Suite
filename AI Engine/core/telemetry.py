import json
import os
import uuid
import time
from datetime import datetime

class TelemetryManager:
    """
    Centralized Observability Manager for Optimax AI Engine.
    Handles structured logging, metrics collection, and trace propagation.
    """
    def __init__(self):
        self.base_dir = os.path.join(os.path.dirname(__file__), "..", "src", "data")
        self.metrics_dir = os.path.join(self.base_dir, "metrics")
        self.logs_dir = os.path.join(self.base_dir, "logs")
        
        # Ensure directories exist
        for d in [self.metrics_dir, self.logs_dir]:
            if not os.path.exists(d):
                os.makedirs(d)

    def generate_trace_id(self) -> str:
        return str(uuid.uuid4())

    def log_event(self, decision_id: str, stage: str, level: str, message: str, extra: dict = None):
        """Standardized Structured JSON Logging."""
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "decision_id": decision_id,
            "stage": stage,
            "level": level,
            "message": message,
            "metadata": extra or {}
        }
        
        log_file = os.path.join(self.logs_dir, "engine.jsonl")
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(json.dumps(log_entry) + "\n")

    def record_metrics(self, decision_id: str, metrics: dict):
        """Records performance and operational metrics."""
        entry = {
            "timestamp": datetime.now().isoformat(),
            "decision_id": decision_id,
            "metrics": metrics
        }
        
        # We store daily metrics files to avoid single-file bloat
        date_str = datetime.now().strftime("%Y%m%d")
        metrics_file = os.path.join(self.metrics_dir, f"metrics_{date_str}.jsonl")
        
        with open(metrics_file, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry) + "\n")

    def log_failure(self, decision_id: str, stage: str, error: Exception):
        """Explicit failure visibility."""
        failure_entry = {
            "timestamp": datetime.now().isoformat(),
            "decision_id": decision_id,
            "failure_stage": stage,
            "error_type": type(error).__name__,
            "error_message": str(error)
        }
        
        # Log to the main engine log at ERROR level
        self.log_event(decision_id, stage, "ERROR", str(error))
        
        # Also store in a specific failure log for high visibility
        fail_file = os.path.join(self.logs_dir, "failures.jsonl")
        with open(fail_file, "a", encoding="utf-8") as f:
            f.write(json.dumps(failure_entry) + "\n")
