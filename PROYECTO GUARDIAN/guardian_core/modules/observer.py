import time
from typing import Generator
from .models import Anomaly

class GuardianObserver:
    """
    Monitors system state (mocks log ingestion for MVP).
    """
    
    def listen_for_anomalies(self) -> Generator[Anomaly, None, None]:
        """
        Simulates listening to a log stream.
        Yields an anomaly when 'detected'.
        """
        print("[Observer] Monitoring log streams...")
        time.sleep(1) # Simulate monitoring time
        
        # MOCK: Specific scenario detection
        # Logic: We pretend we parsed a log line like "CRITICAL: DB Connection Refused"
        
        print("[Observer] ! ALERT DETECTED in logs.")
        
        yield Anomaly(
            id="ERR-500-DB",
            description="Error 500 – Conexión rechazada en Base de Datos",
            timestamp=time.strftime("%Y-%m-%d %H:%M:%S"),
            severity="critical",
            context={
                "service": "database",
                "last_error": "ConnectionRefusedError: port 5432",
                "duration": "2m"
            }
        )
