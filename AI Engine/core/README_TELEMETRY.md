# Optimax AI Engine: Telemetry & Observability Guide

## 📡 The Observability Stack
Optimax AI Engine implements a **local-first, structured observability system** designed for high-performance and high-traceability environments.

## 1. Decision Tracing (UUID)
Every time the engine starts, it generates a unique `decision_id` (UUIDv4). This ID serves as a **Correlation ID** that bridges the gap between the Python AI Engine and the PowerShell Windows Agent.
- **Trace Propagation**: The ID is passed from the Engine JSON output to the Agent's script invoker.
- **Audit Consistency**: All logs and performance metrics share this ID, allowing you to reconstruct the entire "thought-to-execution" process.

## 2. Structured Logging (`src/data/logs/`)
We use **JSONL (JSON Lines)** format for production-grade logs.
- `engine.jsonl`: Tracks the internal lifecycle of the AI decision pipeline (Context loading, AI requests, Safety Gate triggers).
- `execution.jsonl`: Tracks the PowerShell script execution, providing success/fail status and durations.
- `failures.jsonl`: High-visibility log for critical errors at any stage.

**Example Log Entry:**
```json
{
  "timestamp": "2026-01-20T23:01:45.123Z",
  "decision_id": "550e8400-e29b-41d4-a716-446655440000",
  "stage": "ai_decision",
  "level": "INFO",
  "message": "Requesting LLM decision"
}
```

## 3. Metrics Layer (`src/data/metrics/`)
Operational metrics are stored separately to allow for performance analysis without parsing heavy log files.
- `metrics_YYYYMMDD.jsonl`: Stores performance data per decision.
  - `total_duration_sec`: Total time from engine start to plan output.
  - `ai_latency_sec`: Time spent waiting for the LLM provider.
  - `actions_proposed/executed`: Quantifies the impact and efficiency of the decision.

## 4. Failure Visibility
Failures are categorized by **Failure Stage**:
1. `context`: Errors gathering system info.
2. `ai_decision`: Connectivity or AI reasoning errors.
3. `validation`: Schema or Safety Gate rejections.
4. `execution`: PowerShell runtime errors.

## 🛠 How to Analyze
To view the latest execution trace:
```powershell
# Get latest decision ID from logs
$lastId = (Get-Content src/data/logs/engine.jsonl -Tail 1 | ConvertFrom-Json).decision_id

# Find all related events
Get-Content src/data/logs/*.jsonl | ConvertFrom-Json | Where-Object { $_.decision_id -eq $lastId }
```
