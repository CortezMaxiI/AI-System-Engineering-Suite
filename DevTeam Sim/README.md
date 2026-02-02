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

### 📝 Final Note
> **Notice**: This project is a documentation-driven design exercise. It demonstrates senior-level skills in system modeling, AI agent strategy, and technical writing. No functional code is provided as the intent is to showcase the **conceptual foundation and architectural rigor** required to build complex AI-driven simulations.
>
> **Nota**: Este proyecto es un ejercicio de diseño basado en documentación. Demuestra habilidades de nivel senior en modelado de sistemas, estrategia de agentes de IA y redacción técnica. No se proporciona código funcional, ya que la intención es mostrar la **base conceptual y el rigor arquitectónico** necesarios para construir simulaciones complejas impulsadas por IA.

