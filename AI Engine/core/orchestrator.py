import sys
import os
import json
import time
from decision_core import DecisionCore
from script_generator import ScriptGenerator
from telemetry import TelemetryManager

class EngineOrchestrator:
    def __init__(self, telemetry=None):
        self.telemetry = telemetry or TelemetryManager()
        self.brain = DecisionCore(telemetry=self.telemetry)
        self.generator = ScriptGenerator()

    def run(self, context_path, decision_id=None, demo_mode=False):
        start_time = time.time()
        if not decision_id:
            decision_id = self.telemetry.generate_trace_id()

        # 1. Load Context
        try:
            self.telemetry.log_event(decision_id, "context", "INFO", f"Loading context (Demo: {demo_mode}) from {context_path}", {"demo_mode": demo_mode})
            with open(context_path, 'r', encoding='utf-8-sig') as f:
                context_data = json.load(f)
        except Exception as e:
            self.telemetry.log_failure(decision_id, "context", e)
            raise RuntimeError(f"Failed to load context: {str(e)}")

        # 2. Make Decision
        decision = self.brain.analyze_context(context_data, decision_id=decision_id)

        # 3. Generate Scripts
        executable_scripts = self.generator.generate_scripts(decision)

        # 4. Final Output Construction
        final_output = {
            "meta": {
                "decision_id": decision_id,
                "demo_mode": demo_mode,
                "model": f"{self.brain.provider.provider}/{self.brain.provider.model}",
                "prompt_version": decision.get("prompt_version", "unknown"),
                "safety_status": "Override-Active" if decision.get("safety_override") else "Nominal"
            },
            "strategy": decision["strategy"],
            "confidence_score": decision.get("confidence_score"),
            "risk_level": decision.get("risk_level"),
            "reasoning": decision["reasoning"],
            "plan": executable_scripts
        }

        # 5. Record Final Engine Metrics
        total_duration = time.time() - start_time
        metrics = {
            "total_duration_sec": round(total_duration, 3),
            "ai_latency_sec": decision.get("ai_latency_sec", 0),
            "actions_proposed": len(decision.get("actions", [])),
            "actions_executable": len(executable_scripts)
        }
        self.telemetry.record_metrics(decision_id, metrics)
        self.telemetry.log_event(decision_id, "engine_complete", "INFO", "Engine cycle finished successfully", metrics)

        return final_output

if __name__ == "__main__":
    # For backward compatibility if someone runs this directly
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--context', type=str, required=True)
    parser.add_argument('--demo', action='store_true')
    args = parser.parse_args()
    
    orchestrator = EngineOrchestrator()
    result = orchestrator.run(args.context, demo_mode=args.demo)
    print(json.dumps(result, indent=2))
