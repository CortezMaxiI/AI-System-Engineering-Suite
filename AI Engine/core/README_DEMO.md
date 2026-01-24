# Optimax AI Engine: Showcase & Demo Mode

## 📽️ The Purpose of Demo Mode
To facilitate safe demonstrations for recruiters, stakeholders, and technical reviewers, Optimax AI Engine includes a native **Showcase (DEMO) Mode**. This allows the full AI decision pipeline to run without applying any actual mutations to the host Windows system.

## 🚀 How to Activate

### Option 1: PowerShell Flag (Recommended for local testing)
Run the integration test with the `-Demo` switch:
```powershell
powershell -ExecutionPolicy Bypass -File tests/integration_test.ps1 -Demo
```

### Option 2: Environment Variable (Global)
Set the following variable in your session:
```powershell
$env:OPTIMAX_DEMO_MODE = "true"
```

### Option 3: Python CLI
If calling the engine directly:
```bash
python src/engine/engine.py --context your_context.json --demo
```

## 🛡️ What happens in Demo Mode?
1.  **Context Gathering**: Hardware telemetry is collected normally to feed the AI.
2.  **AI Reasoning**: The LLM analyzes the system and proposes a strategy based on real data.
3.  **Safety Gates**: Risk and confidence assessments are performed and logged.
4.  **Simulated Execution**: The PowerShell agent receives the optimization plan but **skips all commands**. It logs a simulation entry and returns a specialized "Success (Simulated)" status.
5.  **Full Observability**: All audit logs, telemetry, and metrics are generated as if the system were live.

## 📊 How to Verify Simulation
Open the execution logs at `src/data/logs/execution.jsonl`. Every entry will contain the `demo_mode: true` field:

```json
{
  "timestamp": "2026-01-20T23:07:15.123Z",
  "decision_id": "8432-...",
  "demo_mode": true,
  "level": "INFO",
  "message": "DEMO MODE: Simulating execution..."
}
```

This ensures that the system is **Safe-by-Design** for any technical showcase or portfolio review.
