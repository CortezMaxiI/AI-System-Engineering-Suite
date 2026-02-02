🛡️ Guardian — AI-Assisted SRE First Responder






Guardian is an experimental AI-assisted observability and response system designed as a first responder for infrastructure failures.

The project is built around a single core principle:

“Protect — do not blindly automate.”

Guardian never executes actions autonomously.
It observes, reasons, simulates, and requires explicit human validation before any change is applied.

🎯 Project Objective

Reduce the gap between:

detection of a critical infrastructure failure

and qualified human intervention

by providing explainable diagnostics, safe simulations, and verified mitigation proposals.

This project prioritizes judgment, safety, and traceability over aggressive automation.

⛓️ The Decision Chain

Guardian follows a strict, auditable path from anomaly detection to proposed resolution.
Every step is verifiable and traceable.

graph TD
    A[🚨 Anomaly Detected] --> B[🧠 Brain Analysis]
    B --> C[📝 Mitigation Plan]
    C --> D[🧪 Sandbox Simulation]
    D -- Success --> E[🛡️ Security Gate]
    D -- Failure --> F[❌ Reject Action]
    E --> G[🧑‍💻 Human Validation]
    G -- Approved --> H[🚀 Production Execution]
    G -- Rejected --> I[⏹️ Aborted]


Flow explanation:

Anomaly — Detection of irregular patterns in logs or metrics

Reasoning — AI generates a root cause hypothesis and mitigation plan

Simulation — Proposed actions are tested in an isolated mirror environment

Simulation Result — Only a 100% successful simulation allows progression

🧠 Design Philosophy

AI is not an authority

No action can be executed without prior simulation

Humans always retain final control

The system explains:

what it detected

what it reasoned

what it tested

and the resulting outcome

Guardian is designed as an SRE co-pilot, not an execution bot.

🔐 Security Gate — Core Pillar

Guardian enforces a mandatory Security Gate implemented through Python decorators.
This mechanism is the backbone of its safety model.

How it works:

Forced Validation — Production execution methods are decorated with @require_simulation

Active Blocking — If a plan reaches execution without passing the Sandbox, or if the SimulationResult is negative, execution is automatically blocked

Immutable by Design — This rule is enforced at code level, preventing human omission or bypass

This guarantees that no unsafe action can reach production.

🧩 System Architecture

Guardian is composed of independent modules, each with a single, well-defined responsibility:

👁️ Observer

Monitors events (logs / alerts — mocked in the MVP)

Detects anomalies and normalizes them into an Anomaly object

🧠 Brain

Analyzes anomalies and generates a root cause hypothesis

Produces a MitigationPlan with explicit commands and risk levels

🧪 Sandbox

Executes proposed actions in an isolated environment

Validates configuration integrity and health checks before reporting

🧑‍💻 Interface

Presents full reasoning and simulation results to the human operator

Requires explicit approval before any production execution

▶️ MVP Execution
# Install dependencies
pip install -r requirements.txt

📝 Final Note

Notice: Guardian is intentionally conservative by design.
It demonstrates a safety-first approach to AI-assisted SRE workflows, focusing on decision quality, traceability, and human-in-the-loop control, rather than full automation.

# Ejecutar el núcleo de Guardian
python guardian_core/main.py
```

