from functools import wraps
from typing import Dict
from .models import MitigatedPlan, SimulationResult

def require_simulation(func):
    """
    Security Decorator: Blocks execution if the plan hasn't passed simulation.
    """
    @wraps(func)
    def wrapper(self, plan: MitigatedPlan, simulation_result: SimulationResult, *args, **kwargs):
        if not simulation_result or not simulation_result.passed:
            print(f"\n[SECURITY BLOCK] Action '{plan.action_id}' REJECTED. Simulation failed or not run.")
            print(f"Reason: {simulation_result.details if simulation_result else 'No simulation record'}")
            return False
        return func(self, plan, simulation_result, *args, **kwargs)
    return wrapper

class GuardianSandbox:
    """
    Simulates actions in a safe environment.
    """
    
    def run_simulation(self, plan: MitigatedPlan) -> SimulationResult:
        print(f"\n[Sandbox] Initializing container logic for action: {plan.action_id}...")
        print(f"[Sandbox] Simulating command: '{plan.command}' on target '{plan.target_service}'")
        
        # MOCK: Logic to determine success
        # if command is restart and service is database -> Success
        
        if "restart" in plan.command and "database" in plan.target_service:
            print("[Sandbox] Verifying config files... OK")
            print("[Sandbox] Simulating service stop... OK")
            print("[Sandbox] Simulating service start... OK")
            print("[Sandbox] Checking health endpoint... 200 OK")
            
            return SimulationResult(
                passed=True,
                details="Simulation successful. Service recovered in 2s.",
                logs=["Stop OK", "Start OK", "Health Check OK"]
            )
        else:
             return SimulationResult(
                passed=False,
                details="Simulation failed. Unknown command or side effects detected.",
                logs=["Command detection error"]
            )
