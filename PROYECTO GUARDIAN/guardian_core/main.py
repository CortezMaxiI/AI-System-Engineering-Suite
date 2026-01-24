import sys
from modules.observer import GuardianObserver
from modules.brain import GuardianBrain
from modules.sandbox import GuardianSandbox, require_simulation
from modules.models import Anomaly, MitigatedPlan, SimulationResult

class GuardianInterface:
    def __init__(self):
        self.observer = GuardianObserver()
        self.brain = GuardianBrain()
        self.sandbox = GuardianSandbox()

    def display_panel(self, title: str, content: str):
        print("\n" + "="*50)
        print(f" {title.upper()} ".center(50, "-"))
        print(content)
        print("="*50)

    @require_simulation
    def execute_in_production(self, plan: MitigatedPlan, simulation_result: SimulationResult):
        """
        Final execution step. Only reachable if simulation passed (via decorator).
        Note: In MVP, this just simulates the SUCCESS message without real action.
        """
        self.display_panel("Production Execution", f"[REAL-TIME] Executing: {plan.command} on {plan.target_service}...")
        print("\n[SUCCESS] Action completed. Verification successful. System stable.")
        return True

    def run_mvp_flow(self):
        print("\n🚀 Starting GUARDIAN CORE MVP...")
        
        # 1. OBSERVE
        for anomaly in self.observer.listen_for_anomalies():
            self.display_panel("Anomaly Detected", 
                f"ID: {anomaly.id}\n"
                f"Problem: {anomaly.description}\n"
                f"Severity: {anomaly.severity.upper()}\n"
                f"Context: {anomaly.context.get('last_error')}")

            # 2. CONTEXTUALIZE & THINK (BRAIN)
            plan = self.brain.analyze(anomaly)
            self.display_panel("Brain Proposal", 
                f"Hypothesis: {plan.reasoning}\n"
                f"Proposed Action: {plan.description}\n"
                f"Target: {plan.target_service}\n"
                f"Command: {plan.command}\n"
                f"Risk Level: {plan.risk_level.upper()}")

            # 3. SIMULATE (SANDBOX)
            simulation_result = self.sandbox.run_simulation(plan)
            
            sim_status = "✅ SUCCESS" if simulation_result.passed else "❌ FAILED"
            self.display_panel("Sandbox Results", 
                f"Status: {sim_status}\n"
                f"Details: {simulation_result.details}\n"
                f"Logs: {', '.join(simulation_result.logs)}")

            if not simulation_result.passed:
                print("\n[!] GUARDIAN: Emergency rejection. Reason: Simulation failed. Human manual intervention required.")
                continue

            # 4. REPORT & HUMAN DECISION
            print(f"\n[REPORT] Detecté '{anomaly.description}'.")
            print(f"Probé '{plan.description}' en el sandbox con éxito.")
            decision = input("\n¿Deseas aplicar esta acción en producción? [S/N]: ").strip().upper()

            if decision == 'S':
                self.execute_in_production(plan, simulation_result)
            else:
                print("\n[ACTION ABORTED] User rejected the proposal. Keeping monitoring active.")

if __name__ == "__main__":
    guardian = GuardianInterface()
    try:
        guardian.run_mvp_flow()
    except KeyboardInterrupt:
        print("\n\n[SYSTEM] Guardian shutting down gracefully.")
        sys.exit(0)
