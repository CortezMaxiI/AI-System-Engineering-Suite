# 🤖 DevTeam Sim
### AI-Driven Development Team Simulator: Modeling Systemic Friction through Cognitive Agents

![Python 3.11+](https://img.shields.io/badge/Python-3.11+-blue.svg)
![Multi-Agent System](https://img.shields.io/badge/Architecture-Multi--Agent-orange.svg)
![Asynchronous Logic](https://img.shields.io/badge/Logic-Asynchronous-green.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## 🇺🇸 English Version

### 🎯 Overview
**DevTeam Sim** is a conceptual simulation engine designed to model the complex decision-making dynamics within software engineering environments. Unlike traditional project management tools, this system focuses on **systemic thinking**, **technical causality**, and **conflict management** between AI agents with divergent interests and persistent biases.

### ⚠️ The Problem
In professional software engineering, technical failure is rarely caused by code alone. It is driven by **flawed systemic dynamics**. Decisions are made under pressure, with conflicting priorities, and burdened by the weight of previous technical debt. Conventional tools (Jira, GitHub) track *what* is being done, but they fail to model *how* today's shortcuts constraint tomorrow's options.

### 🧩 What it is (and what it is NOT)
| ✅ What it is | ❌ What it is NOT |
| :--- | :--- |
| A cognitive state simulation engine | A project management tool (not a Jira replacement) |
| A framework for biased AI agents | A source code generator or "AI Developer" |
| A model for tracking technical causality | A production automation or CI/CD tool |
| A tool for training technical judgment | A generic chatbot demo |

### 🏛️ Conceptual Architecture
The system is built upon a strict separation of concerns to ensure causal integrity and scalability:

#### 1. State Engine (Deterministic Core)
The project's health is represented by a 4-dimensional state vector:
```python
S = { 
    "Technical Debt", # Accumulation of sub-optimal decisions
    "Team Morale",    # Multiplier for performance and retention
    "Risk",           # Probability of catastrophic failure (bugs, outages)
    "Progress"        # Completion of scenario objectives
}
```

#### 2. Cognitive Agents (The Friction Layer)
Each agent is a specialized AI entity with a unique utility function and persistent cognitive biases:
*   **Tech Lead**: Optimizes for stability and minimum Technical Debt.
*   **Product Manager**: Optimizes for Progress and time-to-market.
*   **Pragmatic Dev**: Optimizes for implementation simplicity and immediate effort reduction.

#### 3. Decision & Consequence Model
The engine enforces a **Mandatory Trade-off Principle**: If a decision improves one metric, it must adversely affect another, either directly or via **Latent Events** (delayed consequences).

### 🔄 The Agentic Loop
The system operates in discrete cycles where the state evolves through the interplay of human choice and agent friction. This "Agentic Loop" is governed by a state transition model that ensures every action has a traceable technical cost.

1.  **State Presentation (S_t)**: The user receives the current project metrics and active latent events.
2.  **Cognitive Friction (Debate)**: Agents analyze the current dilemma. The Product Manager pushes for velocity; the Tech Lead warns of debt; the Dev offers a "middle ground" shortcut.
3.  **Human Intervention**: The user makes a decision, choosing which technical or human cost to incur.
4.  **Causal Impact**: The engine applies direct deltas to the state vector and calculates the probability of triggering latent events or random entropy (incidents).
5.  **New State (S_t+1)**: Metrics are updated, and the cycle repeats.

*For a detailed look at the transitions, see [04_STATE_TRANSITION_MODEL.md](./docs/04_STATE_TRANSITION_MODEL.md).*

### 📂 Project Documentation
This repository is structured as a technical audit and design specification:
1.  **[01_SRS_DevTeam_Sim.MD](./docs/01_SRS_DevTeam_Sim.MD)**: Vision, scope, and mathematical foundation.
2.  **[02_DESIGN_DECISIONS.md](./docs/02_DESIGN_DECISIONS.md)**: Resolution of structural ambiguities and scaling constraints.
3.  **[03_COGNITIVE_AGENTS.md](./docs/03_COGNITIVE_AGENTS.md)**: Deep dive into agent behaviors, biases, and relational memory.
4.  **[04_STATE_TRANSITION_MODEL.md](./docs/04_STATE_TRANSITION_MODEL.md)**: The causal logic governing direct impacts and latent triggers.
5.  **[05_PORTFOLIO_PRESENTATION.md](./docs/05_PORTFOLIO_PRESENTATION.md)**: Case study overview for hiring managers and tech leads.

### 🚀 What This Project Demonstrates
*   **Systems Design**: Ability to model non-linear systems and technical causality.
*   **AI Agent Architecture**: Designing prompts that force consistency, friction, and "character" over generic LLM compliance.
*   **Critical Thinking**: Deep understanding of the trade-offs that define real-world engineering leadership.

---

## 🇪🇸 Versión en Español

### 🎯 Visión General
**DevTeam Sim** es un motor de simulación conceptual diseñado para modelar la dinámica de toma de decisiones en entornos de ingeniería de software. A diferencia de las herramientas de gestión tradicionales, este sistema se centra en el **pensamiento sistémico**, la **causalidad técnica** y la **gestión de conflictos** entre agentes de IA con intereses contrapuestos y sesgos persistentes.

### ⚠️ El Problema
En la ingeniería de software profesional, el fallo técnico rara vez es causado solo por el código. Es impulsado por **dinámicas sistémicas fallidas**. Las decisiones se toman bajo presión, con prioridades en conflicto y bajo el peso de la deuda técnica previa. Las herramientas convencionales (Jira, GitHub) rastrean *qué* se hace, pero fallan en modelar *cómo* los atajos de hoy restringen las opciones del mañana.

### 🧩 Qué es (y qué NO es)
| ✅ Qué es | ❌ Qué NO es |
| :--- | :--- |
| Un motor de simulación de estado cognitivo | Un gestor de proyectos (no reemplaza a Jira) |
| Un framework de agentes de IA con sesgos | Un generador de código o "AI Developer" |
| Un modelo de trazabilidad de causalidad técnica | Una herramienta de automatización o CI/CD |
| Una herramienta para entrenar el juicio técnico | Una demo genérica de chatbot |

### 🏛️ Arquitectura Conceptual
El sistema se basa en una separación estricta de responsabilidades para garantizar la integridad causal:

#### 1. Motor de Estado (Núcleo Determinista)
La salud del proyecto se representa mediante un vector de estado de 4 dimensiones:
```python
S = { 
    "Deuda Técnica", # Acumulación de decisiones subóptimas
    "Moral del Equipo", # Multiplicador de rendimiento y retención
    "Riesgo",         # Probabilidad de fallos catastróficos
    "Progreso"        # Finalización de objetivos del escenario
}
```

#### 2. Agentes Cognitivos (Capa de Fricción)
Cada agente es una entidad de IA especializada con una función de utilidad única y sesgos cognitivos persistentes:
*   **Tech Lead**: Optimiza estabilidad y mínima Deuda Técnica.
*   **Product Manager**: Optimiza Progreso y velocidad de entrega.
*   **Dev Pragmático**: Optimiza simplicidad de implementación y reducción de esfuerzo inmediato.

#### 3. Modelo de Decisión y Consecuencia
El motor impone un **Principio de Trade-off Obligatorio**: Si una decisión mejora una métrica, debe afectar negativamente a otra, ya sea de forma directa o mediante **Eventos Latentes** (consecuencias diferidas).

### 🔄 El Bucle Agéntico (Agentic Loop)
El sistema opera en ciclos discretos donde el estado evoluciona mediante la interacción de las decisiones humanas y la fricción de los agentes.

1.  **Presentación de Estado (S_t)**: El usuario recibe las métricas actuales y los eventos latentes activos.
2.  **Fricción Cognitiva (Debate)**: Los agentes exponen sus posturas. El Tech Lead advierte sobre la deuda; el PM presiona por el deadline.
3.  **Intervención Humana**: El usuario toma una decisión consciente de los trade-offs.
4.  **Impacto Causal**: El motor aplica los cambios al estado y evalúa la activación de consecuencias diferidas.
5.  **Nuevo Estado (S_t+1)**: Se actualizan las métricas y comienza un nuevo ciclo.

### 📂 Cómo leer el proyecto
Este repositorio se estructura como una auditoría técnica y especificación de diseño:
1.  **[01_SRS_DevTeam_Sim.MD](./docs/01_SRS_DevTeam_Sim.MD)**: Visión, alcance y bases matemáticas.
2.  **[02_DESIGN_DECISIONS.md](./docs/02_DESIGN_DECISIONS.md)**: Resolución de ambigüedades estructurales y restricciones de escala.
3.  **[03_COGNITIVE_AGENTS.md](./docs/03_COGNITIVE_AGENTS.md)**: Análisis profundo de comportamientos, sesgos y memoria relacional.
4.  **[04_STATE_TRANSITION_MODEL.md](./docs/04_STATE_TRANSITION_MODEL.md)**: Lógica causal que gobierna impactos directos y triggers latentes.
5.  **[05_PORTFOLIO_PRESENTATION.md](./docs/05_PORTFOLIO_PRESENTATION.md)**: Caso de estudio para reclutadores y líderes técnicos.

### 🚀 Qué demuestra el proyecto
*   **Diseño de Sistemas**: Capacidad para modelar sistemas no lineales y causalidad técnica.
*   **Arquitectura de Agentes de IA**: Diseño de prompts que fuerzan consistencia, fricción y "personalidad" sobre la complacencia típica de los LLM.
*   **Pensamiento Crítico**: Profunda comprensión de los trade-offs que definen el liderazgo de ingeniería en el mundo real.

---

### 📍 Project Status / Estado del Proyecto
**Concept & Design Phase (Complete)**. This project is currently a formal architectural and cognitive design specification. Implementation of the execution engine and Agent API is out of the current scope.

**Fase de Concepto y Diseño (Completada)**. Este proyecto es actualmente una especificación formal de diseño arquitectónico y cognitivo. La implementación del motor de ejecución y la API de Agentes está fuera del alcance actual.

### ✒️ Author / Autor
**[Maxi]** - *AI Systems Architect & Software Engineer*

---

### 📝 Final Note / Nota Final
> **Notice**: This project is a documentation-driven design exercise. It demonstrates senior-level skills in system modeling, AI agent strategy, and technical writing. No functional code is provided as the intent is to showcase the **conceptual foundation and architectural rigor** required to build complex AI-driven simulations.
>
> **Nota**: Este proyecto es un ejercicio de diseño basado en documentación. Demuestra habilidades de nivel senior en modelado de sistemas, estrategia de agentes de IA y redacción técnica. No se proporciona código funcional, ya que la intención es mostrar la **base conceptual y el rigor arquitectónico** necesarios para construir simulaciones complejas impulsadas por IA.
