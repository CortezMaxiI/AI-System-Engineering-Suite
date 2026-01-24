import json
import os
import datetime
import time
from llm_provider import LLMProvider
from telemetry import TelemetryManager

class DecisionCore:
    """
    Hardenized AI Decision Engine.
    Implements Safety Gates, Audit Logging, and Fallback Transparency.
    """

    def __init__(self, telemetry: TelemetryManager = None):
        self.provider = LLMProvider()
        self.telemetry = telemetry or TelemetryManager()
        self.prompt_path = os.path.join(os.path.dirname(__file__), "prompts", "system_prompt_v1.txt")
        self.audit_log_dir = os.path.join(os.path.dirname(__file__), "..", "src", "data", "audit")
        
        # Load System Prompt
        try:
            with open(self.prompt_path, 'r', encoding='utf-8') as f:
                self.system_prompt = f.read()
        except Exception as e:
            self.system_prompt = f"ERROR: Could not load prompt file at {self.prompt_path}. {str(e)}"

    def analyze_context(self, context_json: dict, decision_id: str = "unknown") -> dict:
        """
        Main decision pipeline: Reasoning -> Safety Gate -> Audit.
        """
        user_prompt = f"System Context JSON:\n{json.dumps(context_json, indent=2)}"
        timestamp = datetime.datetime.now().isoformat()
        start_time = time.time()
        
        try:
            if "ERROR" in self.system_prompt:
                 raise FileNotFoundError(self.system_prompt)

            # 1. AI Reasoning Request
            self.telemetry.log_event(decision_id, "ai_decision", "INFO", "Requesting LLM decision")
            decision = self.provider.call(self.system_prompt, user_prompt)
            
            latency = time.time() - start_time
            decision["ai_latency_sec"] = round(latency, 3)

            # 2. Schema Validation
            self._validate_schema(decision)
            
            # 3. Decision Safety Gate (Pre-execution validation)
            decision = self._apply_safety_gate(decision, decision_id)
            
            # 4. Success Log
            self._log_audit(decision, context_json, "success", timestamp, decision_id)
            
            return decision

        except Exception as e:
            # 5. Fallback Transparency & Logging
            self.telemetry.log_failure(decision_id, "ai_decision", e)
            fallback_decision = self._handle_fallback(e, context_json, timestamp, decision_id)
            return fallback_decision

    def _validate_schema(self, decision: dict):
        required = ["strategy", "confidence_score", "risk_level", "reasoning", "actions", "prompt_version"]
        for field in required:
            if field not in decision:
                raise ValueError(f"LLM response missing critical field: {field}")

    def _apply_safety_gate(self, decision: dict, decision_id: str) -> dict:
        """
        Implements Decision Safety Gate: 
        If risk is high and confidence is low (< 0.7), downgrade actions.
        """
        risk = decision.get("risk_level", "low").lower()
        confidence = decision.get("confidence_score", 0.0)
        
        if risk == "high" and confidence < 0.7:
            self.telemetry.log_event(decision_id, "safety_gate", "WARNING", "Safety Gate Triggered: High risk with low confidence")
            decision["safety_override"] = True
            decision["override_reason"] = f"Safety Gate Triggered: High risk ({risk}) with insufficient confidence ({confidence}). Actions downgraded."
            # Only keep low-risk actions
            decision["actions"] = [a for a in decision["actions"] if a.get("risk", "high").lower() == "low"]
            decision["strategy"] = f"{decision['strategy']} (Safety Limited)"
            
        return decision

    def _log_audit(self, decision: dict, context: dict, status: str, timestamp: str, decision_id: str):
        """Records the decision process for auditability."""
        log_entry = {
            "timestamp": timestamp,
            "decision_id": decision_id,
            "status": status,
            "model_metadata": {
                "provider": self.provider.provider,
                "model": self.provider.model,
                "prompt_version": decision.get("prompt_version", "unknown")
            },
            "decision": decision,
            "context_snapshot": context
        }
        
        log_filename = f"decision_{decision_id}.json"
        log_path = os.path.join(self.audit_log_dir, log_filename)
        
        try:
            if not os.path.exists(self.audit_log_dir):
                os.makedirs(self.audit_log_dir)
            with open(log_path, 'w', encoding='utf-8') as f:
                json.dump(log_entry, f, indent=2)
            self.telemetry.log_event(decision_id, "audit", "INFO", f"Audit log created: {log_filename}")
        except Exception as e:
            self.telemetry.log_event(decision_id, "audit", "ERROR", f"Failed to write audit log: {str(e)}")

    def _handle_fallback(self, error: Exception, context: dict, timestamp: str, decision_id: str) -> dict:
        """Transparent fallback when AI fails."""
        reason = "unknown"
        if "API" in str(error) or "requests" in str(error).lower(): reason = "api_error"
        elif "JSON" in str(error) or "schema" in str(error).lower(): reason = "invalid_schema"
        elif "FileNotFound" in str(error): reason = "missing_prompt"
        
        fallback_decision = {
            "decision_id": decision_id,
            "strategy": "Recovery Mode (Safe Baseline)",
            "confidence_score": 1.0,
            "risk_level": "low",
            "prompt_version": "fallback_v1",
            "reasoning": f"AI Engine Fallback activated. Reason: {reason} ({str(error)}). Applying safest possible state.",
            "actions": [
                {"type": "clear_temp_files", "risk": "low", "impact": "low"}
            ],
            "fallback_meta": {
                "error": str(error),
                "reason_code": reason,
                "timestamp": timestamp
            }
        }
        
        self.telemetry.log_event(decision_id, "fallback", "WARNING", f"Engine entering fallback mode: {reason}")
        self._log_audit(fallback_decision, context, "fallback", timestamp, decision_id)
        return fallback_decision
