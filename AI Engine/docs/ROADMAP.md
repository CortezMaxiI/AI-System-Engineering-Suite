# Optimax AI Engine - Technical Roadmap

**Status**: v1.0 (MVP) Complete - [x] Architecture / [x] Core AI / [x] Safety Gates
**Focus**: Stability, Observability, and modular expansion.

## 1. Short-Term: Visualization & Developer Experience (v1.1 - v1.2)
*Focus: Making the "black box" visible.*

- **Dashboard UI (v1.1)**:
  - Build a lightweight web interface (React/Next.js) to consume the `metrics/*.jsonl` and `failures.jsonl`.
  - Visualization of "Confidence vs Risk" scatter plots for recent decisions.
- **Enhanced Safety Policies (v1.2)**:
  - Implement a `dry-run` validation for generated scripts using a safer sandbox or a syntax checker (e.g., `PSScriptAnalyzer`) before execution.
  - Add "User Confirmation" mode for High-Risk actions, even if confidence is high.
- **CLI Improvements**:
  - Interactive mode for the Python engine to test prompts without running the full agent.

## 2. Medium-Term: Plugin Architecture & Local Inference
*Focus: Reducing dependency on external APIs and increasing versatility.*

- **SLM Integration (Small Language Models)**:
  - Experiment with running local models (e.g., Phi-3, Mistral) via ONNX or `llama.cpp` to replace the cloud provider.
  - **Goal**: Zero-latency, privacy-first decision making without internet requirement.
- **Plugin System**:
  - Decouple the monolithic `script_generator.py`.
  - Create a plugin interface (`IPerformanceModule`) allowing third-party developers to write optimization modules (e.g., `NetworkOptimizer`, `StorageTrimmer`) that the AI can invoke.
- **Contextual Profiles**:
  - AI should detect specific workloads (e.g., "Compiling Code", "Rendering Video", "Gaming") and load distinct system prompts optimized for those scenarios.

## 3. Long-Term: Policy & Governance
*Focus: Enterprise-grade control and explainability.*

- **Policy-as-Code**:
  - Allow administrators to define strict boundaries (e.g., "Never disable Defender", "Max CPU throttling 10%") that overrule any AI decision.
- **Explainable AI (XAI)**:
  - Move beyond simple reasoning strings. Implement chain-of-thought logging where the AI cites specific documentation or telemetry data points that led to a decision.
- **Feedback Reinforcement Learning**:
  - Implement a closed loop where post-execution metrics (did FPS actually increase?) feed back into a vector database to fine-tune future prompts (RAG for Optimization).

## 4. Non-Goals
*Explicit boundaries to maintain engineering integrity.*

- **NO "Snake Oil" Tweaks**: We will not implement placebo registry hacks (e.g., `TcpAckFrequency` without network analysis) just to inflate feature counts.
- **NO Kernel Drivers**: The system will remain strictly in user-space/admin-space using native Windows APIs. System stability is paramount.
- **NO Closed Source Logic**: The AI's reasoning must always be auditable. No "proprietary magic binary" blobs.

---
*Roadmap subject to technical review and architectural fit.*
