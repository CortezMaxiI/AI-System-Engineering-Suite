# 🚀 Optimax AI Engine: Responsible AI-First Windows Optimization

![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue?logo=python&logoColor=white)
![PowerShell 7.0+](https://img.shields.io/badge/powershell-7.0%2B-blue?logo=powershell&logoColor=white)
![License MIT](https://img.shields.io/badge/license-MIT-green)

**Optimax AI Engine** is a high-performance technical demonstration of how Large Language Models (LLMs) can be integrated into system-level automation without sacrificing safety or auditability. It moves beyond static scripts by using an AI "Brain" to reason over real-time hardware telemetry and a "Decision Safety Gate" to prevent risky autonomous execution.

---

## 📚 Documentation
For detailed insights into the project's design and goals, refer to the following documents:
- **[System Architecture](docs/ARCHITECTURE.md)**: Technical breakdown of the AI pipeline and safety layers.
- **[Project Roadmap](docs/ROADMAP.md)**: Planned features and evolutionary path.
- **[Requirements Specification](docs/Documento%20de%20Especificaci%C3%B3n%20de%20Requerimientos.md)**: Detailed SRS and functional definitions.

---

## 🎯 Target Audience
- **Who it is for**: Technical recruiters, systems architects, and performance engineers looking for a reference implementation of LLM orchestration in systems programming.
- **Who it is NOT for**: End-users seeking a "one-click" magic booster. This is a developer-centric tech demo focused on architectural integrity.

## ⚠️ The Core Problem
Traditional Windows optimizers often suffer from two critical flaws:
1. **Opaque Legacy Scripts**: Applying static registry tweaks that don't account for modern hardware variations or current system load.
2. **Blind AI Execution**: Modern AI "agents" often operate with too much autonomy, executing code that can lead to system instability if the model hallucinates or misinterprets context.

## 🏛️ The Solution: Architecture of Responsibility
Optimax solves this by implementing a **Hardened AI Pipeline**:

### 1. Decision Safety Gates
AI decisions are not absolute. Every proposal by the LLM is subjected to a local validation layer. If the AI suggests a **High-Risk** action with **Low Confidence** (<0.7), the engine automatically triggers an override, scrubbing the action and logging a safety violation.

### 2. Auditability by Design
Every "thought" and "action" is captured. The system generates structured JSON audit logs containing the full hardware context, the raw AI reasoning, the prompt version used, and the final safety-filtered plan.

### 3. Local-First Philosophy
While the reasoning happens in the cloud (LLM), the execution and observability are strictly local. Native PowerShell agents handle OS interaction, ensuring zero dependency on invasive third-party kernel drivers.

---

## 🛠️ Engineering Highlights

- **LLM Abstraction Layer**: Interchangeable provider support (OpenAI, Gemini, Groq) via a unified interface.
- **Prompt Versioning**: Treating prompts as code. Decisions are tagged with their specific `prompt_version` for full traceability.
- **Decision Tracing (UUID)**: A unique `decision_id` propagates from the Python engine to the PowerShell executor, enabling end-to-end observability.
- **Structured Telemetry**: Machine-parseable JSONL logs track AI latency, execution duration, and risk profiles.

---

## 🔍 How to Evaluate This Project (For Recruiters)

### The "Zero-Risk" Showcase Mode
We have built a dedicated **Demo Mode** so you can run this project on any Windows machine with **zero risk** of registry or system modification.

1. **Set your API Key**: `$env:OPTIMAX_API_KEY = "your_key"`
2. **Run the Showcase**: 
   `powershell -ExecutionPolicy Bypass -File tests/integration_test.ps1 -Demo`
3. **Inspect the Result**: The console and logs will show AI reasoning and simulated actions while keeping your system untouched.

### Key Technical Deep-Dives
When reviewing this codebase, focus on the following design decisions that demonstrate **Senior-Level Thinking**:

1. **Separation of Concerns**: Notice the strict boundary between the **Engine** (Python/Reasoning) and the **Agent** (PowerShell/Execution). The Brain never touches the OS; it only outputs intent.
2. **Resilience & Fallbacks**: Review the `_handle_fallback` logic in `DecisionCore`. The system is designed to fail gracefully, applying a safe baseline if the AI is unreachable or non-deterministic.
3. **Traceability**: Follow a `decision_id` through the `src/data/audit/` and `src/data/logs/` directories to see how the system handles audit trails.
4. **Data-Driven Logic**: The AI doesn't just "run scripts"; it analyzes `context_test.json` (CPU cores, RAM pressure, active processes) before formulating a strategy.

---

## 🚀 Quick Start (Dev Mode)

1. **Set your API Key**: `$env:OPTIMAX_API_KEY = "your_key"`
2. **Run the Integration Test**: 
   `powershell -ExecutionPolicy Bypass -File tests/integration_test.ps1`
3. **Inspect the Audit**: Check `src/data/audit/` for the latest JSON trace.

---
*Developed as a Tech Demo by Maxii. Focused on Architecture, Safety, and AI-First Engineering.*

