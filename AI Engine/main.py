import sys
import os
import ctypes
import json
import argparse
import time

# Ensure core is in path if not already
sys.path.append(os.path.join(os.path.dirname(__file__), 'core'))

from orchestrator import EngineOrchestrator
from telemetry import TelemetryManager

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    except:
        return False

def main():
    # 1. Check Administrator Privileges
    if not is_admin():
        print("[-] ERROR: This script must be run as Administrator to optimize system services.")
        sys.exit(1)

    # 2. Setup Paths
    root_dir = os.path.dirname(os.path.abspath(__file__))
    config_dir = os.path.join(root_dir, 'config')
    profiles_dir = os.path.join(root_dir, 'profiles')
    
    # Ensure mandatory folders exist (Verification task)
    for folder in [config_dir, profiles_dir]:
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"[!] Created missing folder: {folder}")

    # 3. Initialize Engine
    start_time = time.time()
    telemetry = TelemetryManager()
    decision_id = telemetry.generate_trace_id()

    parser = argparse.ArgumentParser(description="Optimax AI Engine - Main Entry")
    parser.add_argument('--context', type=str, required=True, help="Path to context JSON file")
    parser.add_argument('--demo', action='store_true', help="Enable Demo Mode (No real changes)")
    parser.add_argument('--json', action='store_true', help="Output raw JSON result")
    args = parser.parse_args()

    # Verify existing configurations (Relative path check)
    has_config = os.path.exists(os.path.join(root_dir, 'config', 'settings.json'))
    has_profiles = os.path.exists(os.path.join(root_dir, 'profiles', 'gaming.json'))

    demo_mode = args.demo or os.getenv("OPTIMAX_DEMO_MODE", "false").lower() == "true"

    if not args.json:
        print(f"[*] Optimax Engine Starting [ID: {decision_id}]")
        print(f"[*] Root Directory: {root_dir}")
        print(f"[*] Config Found: {'Yes' if has_config else 'No'}")
        print(f"[*] Profiles Found: {'Yes' if has_profiles else 'No'}")
        print(f"[*] Admin Status: Verified")

    # 4. Run Orchestrator
    orchestrator = EngineOrchestrator(telemetry=telemetry)
    try:
        final_output = orchestrator.run(args.context, decision_id=decision_id, demo_mode=demo_mode)
        
        if args.json:
            print(json.dumps(final_output))
            return

        # 5. Output Results
        print("\n" + "="*50)
        print("OPTIMIZATION PLAN GENERATED")
        print("="*50)
        print(f"Strategy:   {final_output['strategy']}")
        print(f"Risk Level: {final_output['risk_level'].upper()}")
        print(f"Confidence: {final_output['confidence_score']*100}%")
        print("-" * 50)
        print(f"Reasoning: {final_output['reasoning']}")
        print("-" * 50)
        
        # Log summary for reporting
        print(f"\n[+] Report: Generated audit log in src/data/audit/decision_{decision_id}.json")
        
        # Finally print the raw JSON for the Agent if needed
        # (Usually main.py is the top level, but for integration tests we might need raw json)
        # print(json.dumps(final_output))

    except Exception as e:
        print(f"[-] Critical Engine Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
