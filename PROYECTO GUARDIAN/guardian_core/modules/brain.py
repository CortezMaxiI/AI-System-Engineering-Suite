from .models import Anomaly, MitigatedPlan

class GuardianBrain:
    """
    The reasoning engine. Analyzes anomalies and proposes solutions.
    """
    
    def analyze(self, anomaly: Anomaly) -> MitigatedPlan:
        print(f"\n[Brain] Analyzing anomaly: {anomaly.id}...")
        
        # MOCK: Semantic reasoning (Hardcoded for MVP Happy Path)
        # In a real system, this would call LLM (Gemini/GPT)
        
        root_cause_hypothesis = "Service process terminated unexpectedly, likely OOM or configuration error."
        reasoning_trace = [
            f"Observed error: {anomaly.description}",
            "Error context implies network refusal.",
            "Historical pattern suggests service requires restart."
        ]
        
        print("[Brain] Hypothesis generated: Service Down.")
        print("[Brain] Formulating mitigation plan...")
        
        return MitigatedPlan(
            action_id="ACT-RESTART-DB",
            description="Reiniciar servicio de Base de Datos",
            target_service="database",
            command="systemctl restart postgresql",
            reasoning=f"Root Cause: {root_cause_hypothesis}. Confidence: High.",
            risk_level="medium"
        )
