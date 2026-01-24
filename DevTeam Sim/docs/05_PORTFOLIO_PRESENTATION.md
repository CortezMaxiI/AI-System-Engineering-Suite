# Portfolio Case Study: DevTeam Sim
## AI-Driven Development Team Simulator

**Proyecto:** DevTeam Sim  
**Rol:** Diseñador de Sistema / Arquitecto de IA  
**Stack Conceptual:** IA Basada en Agentes, Dinámica de Sistemas, Modelado Estocástico  

---

## 1. El Problema: El Costo Invisible de la Toma de Decisiones

En la ingeniería de software profesional, el mayor riesgo no suele ser una tecnología defectuosa, sino la **dinámica sistémica fallida**. Las decisiones técnicas no se toman en el vacío; se toman bajo presión, con intereses contrapuestos y bajo el peso de la deuda técnica previa.

Las herramientas de gestión actuales (Jira, GitHub) son excelentes para rastrear **qué** se hace, pero fallan en modelar **cómo** las decisiones de hoy restringen las opciones del mañana. **DevTeam Sim** aborda este vacío creando un entorno donde el usuario debe navegar la fricción inherente de un equipo de alto rendimiento.

---

## 2. El Enfoque: Simulación Sistémica vs. Asistencia Lineal

### Simulación Sistémica, no Productividad
A diferencia de los simuladores de gestión tradicionales que usan modelos lineales, DevTeam Sim utiliza un **bucle de retroalimentación de estado**. Cada decisión altera un vector de métricas (`TD, M, R, P`) que, a su vez, define el nuevo contexto de decisión. No es una herramienta para "hacer más", sino para entender las consecuencias de lo que se hace.

### IA como Agente con Sesgos, no como Asistente
En la mayoría de las aplicaciones de IA, el objetivo es la utilidad (ayudar al usuario). En DevTeam Sim, el objetivo es la **fricción**. Los agentes de IA se diseñan como "adversarios colaborativos":
- Poseen funciones de utilidad divergentes (Calidad vs. Velocidad vs. Simplicidad).
- Operan bajo sesgos cognitivos persistentes (Aversión al riesgo, sesgo de deadline).
- Desarrollan memoria relacional que afecta su nivel de fricción intra-sesión.

---

## 3. Arquitectura Conceptual

El sistema se basa en una separación estricta de responsabilidades para garantizar coherencia y escalabilidad:

1.  **Motor de Estado (Deterministic Core):** Un modelo matemático que procesa impactos directos y evalúa triggers de eventos latentes. Garantiza que el sistema sea causal y trazable.
2.  **Capa Cognitiva (Agents):** Modelos de lenguaje especializados en roles técnicos que interpretan el estado y abogan por sus métricas prioritarias.
3.  **Capa de Decisión (Interaction):** Un catálogo de escenarios que actúan como "test cases" para la dinámica de equipo.

**Por qué importa esta separación:** Permite que el comportamiento de los agentes evolucione sin alterar la lógica de las métricas, y que la complejidad del escenario crezca sin afectar la estabilidad del motor central.

---

## 4. Qué demuestra este proyecto

Este proyecto no es solo una implementación técnica; es una demostración de pensamiento crítico aplicado al software:

-   **Habilidades de Diseño**: Capacidad para modelar sistemas complejos y abstraer realidades laborales en vectores de estado manejables.
-   **Arquitectura de Agentes**: Diseño de prompts sistémicos que obligan a la IA a mantener consistencia de rol y sesgos, evitando el comportamiento de "complacencia" típico de los LLMs.
-   **Pensamiento Sistémico**: Comprensión de cómo los impactos a corto plazo generan efectos de segundo y tercer orden (evento latente).
-   **Gestión de Producto**: Definición de un MVP claro que aborda el núcleo del problema sin sobrediseñar features periféricas.

---

## 5. Qué NO es este proyecto (Antipatrones de Diseño)

Para entender DevTeam Sim, es crucial definir sus límites:

-   **No es un Gestor de Proyectos:** No importa Jira ni genera tickets. Es un entorno de entrenamiento para el juicio técnico.
-   **No es un Chatbot:** Aunque usa interfaces de lenguaje, la interacción está estructurada. El objetivo es la decisión, no la conversación libre.
-   **No es una Demo de LLM:** El valor reside en las reglas de negocio y el modelo de transición de estados que gobierna a la IA, no en la capacidad de generación del modelo per se.

---

## 6. Evolución del Sistema (Extensiones Futuras)

El diseño actual permite un crecimiento modular sin romper el núcleo sistémico:

-   **Inyección de Escenarios Externos**: Posibilidad de cargar escenarios vía JSON para simular arquitecturas específicas (Microservicios, Legacy, Cloud Migration).
-   **Modo Post-Mortem**: Visualización de grafos causales al final de la sesión para mostrar exactamente qué decisión en el Ciclo N causó el "Incidente Crítico" en el Ciclo N+5.
-   **Expansión de Roles**: Introducción de roles como CISO (Seguridad) o SRE (Disponibilidad) para añadir nuevas dimensiones de conflicto al vector de riesgo.

---

## Conclusión

DevTeam Sim es un experimento en **ingeniería de la fricción**. Demuestra que la IA puede utilizarse no solo para simplificar tareas, sino para modelar la complejidad humana y técnica que define el éxito o fracaso de los proyectos de software modernos.
