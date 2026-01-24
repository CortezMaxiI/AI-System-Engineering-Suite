# Software Requirements Specification (SRS)
## Proyecto: DevTeam Sim – AI-Driven Development Team Simulator

**Versión:** 1.0  
**Fecha:** 22 de enero de 2026  
**Estado:** Definición Técnica  
**Documento:** Especificación de Requerimientos y Arquitectura Conceptual

---

## 1. Introducción y Visión del Sistema
DevTeam Sim es un motor de simulación cognitiva diseñado para modelar la dinámica de toma de decisiones en entornos de ingeniería de software. A diferencia de las herramientas de gestión tradicionales, este sistema se centra en el **pensamiento sistémico**, la **causalidad técnica** y la **gestión de conflictos** entre agentes con intereses contrapuestos.

El sistema opera como un entorno cerrado donde el usuario (Project Lead) interactúa con una arquitectura de agentes de IA que poseen memoria persistente, sesgos profesionales y objetivos divergentes.

### 1.1 Principios de Diseño del Simulador
1.  **Fricción Permanente:** El consenso es costoso y, a menudo, subóptimo. El sistema debe priorizar el debate sobre la concordia.
2.  **Trade-offs Explícitos:** Toda acción técnica tiene un costo humano o de negocio, y viceversa.
3.  **Preservación del Estado:** El proyecto es un sistema dinámico donde las decisiones del pasado restringen las opciones del futuro.
4.  **No-Determinismo Controlado:** Los resultados no son aleatorios, sino estocásticos basados en el riesgo acumulado.

---

## 2. Alcance del Sistema

### 2.1 En Alcance (In-Scope)
* Motor de simulación de estados basado en variables técnicas y humanas.
* Framework de agentes de IA con perfiles psicológicos y técnicos diferenciados.
* Sistema de propagación de consecuencias de corto, medio y largo plazo.
* Modelado de deuda técnica, moral de equipo y riesgo de infraestructura.
* Interfaz de toma de decisiones basada en escenarios y debates.

### 2.2 Fuera de Alcance (Out-of-Scope)
* Generación o ejecución de código fuente real.
* Conexión con APIs de producción o herramientas de CI/CD.
* Automatización de tareas de desarrollo.
* Gestión de proyectos real (no es un reemplazo de Jira o GitHub).

---

## 3. Arquitectura Conceptual de Alto Nivel

El sistema se basa en un bucle de retroalimentación de estado ($State \rightarrow Context \rightarrow Decision \rightarrow Impact \rightarrow New State$).



### 3.1 El Vector de Estado ($S$)
El estado del proyecto en cualquier momento $t$ está definido por:
$$S_t = \{TD, M, R, P\}$$

Donde:
* **$TD$ (Technical Debt):** Acumulación de decisiones subóptimas que incrementan la latencia de futuras decisiones.
* **$M$ (Moral):** Factor multiplicador del rendimiento y la retención del equipo.
* **$R$ (Risk):** Probabilidad de eventos catastróficos (caídas de sistema, bugs críticos).
* **$P$ (Progress):** Porcentaje de finalización de los objetivos del escenario.

### 3.2 Capa de Agentes (Cognitive Layer)
Cada agente opera bajo una función de utilidad distinta:
* **Tech Lead:** Maximiza la estabilidad y minimiza $TD$.
* **Product Manager:** Maximiza $P$ y minimiza el tiempo de entrega.
* **QA Engineer:** Maximiza la visibilidad de $R$.
* **Developer Pragmático:** Maximiza la simplicidad y la velocidad de ejecución inmediata.

---

## 4. Requerimientos Funcionales

| ID | Requerimiento | Descripción |
| :--- | :--- | :--- |
| **RF-01** | **Generación de Escenario** | El sistema debe instanciar un contexto con variables iniciales de presupuesto, tiempo y complejidad técnica. |
| **RF-02** | **Debate de Agentes** | Los agentes deben generar posturas autónomas basadas en sus roles ante un dilema técnico. |
| **RF-03** | **Persistencia Cognitiva** | Los agentes deben recordar decisiones pasadas del usuario, afectando su confianza en el liderazgo. |
| **RF-04** | **Motor de Consecuencias** | Cada decisión debe actualizar el vector de estado $S$ y disparar eventos latentes. |
| **RF-05** | **Feedback Estructurado** | Tras cada ciclo, el sistema entregará un reporte de impacto no comercial, analizando métricas técnicas. |
| **RF-06** | **Inyección de Entropía** | Basado en el nivel de $R$, el sistema generará incidentes imprevistos que interrumpen el flujo planificado. |

---

## 5. Requerimientos No Funcionales

* **RNF-01 (Coherencia de Rol):** El modelo debe garantizar que los agentes no rompan el "personaje" técnico (ej. un QA nunca debería ignorar un riesgo crítico por "ser amable").
* **RNF-02 (Trazabilidad):** El sistema debe registrar el origen de cada incremento en la Deuda Técnica para mostrarlo en el post-mortem.
* **RNF-03 (Baja Latencia de Simulación):** El procesamiento de la lógica de impacto debe ser casi instantáneo tras la entrada del usuario.
* **RNF-04 (Escalabilidad de Escenarios):** La arquitectura debe permitir cargar nuevos JSON de escenario sin modificar el motor central.

---

## 6. Casos de Uso

### UC-01: Gestión de Deuda Técnica vs. Deadline Comercial
1.  **Actor:** Usuario (Líder).
2.  **Contexto:** El Product Manager presiona para lanzar una feature con tests incompletos. El Tech Lead se opone radicalmente.
3.  **Simulación:** El sistema presenta el debate. El usuario puede interrogar a los agentes sobre las consecuencias.
4.  **Decisión:** El usuario decide "Lanzar ahora y arreglar después".
5.  **Impacto:** $P$ aumenta 20%, $TD$ aumenta 40%, $M$ del Tech Lead baja drásticamente. Se crea un "Evento Latente: Fuga de Talento".

---

## 7. Definición del MVP (Minimum Viable Product)

El MVP consistirá en un entorno de ejecución con:
1.  **Motor Core:** Lógica matemática de actualización de métricas.
2.  **3 Agentes:** Tech Lead, Product Manager y Dev Pragmático.
3.  **3 Escenarios:** Refactorización crítica, Lanzamiento bajo presión e Incidente en Producción.
4.  **Output de Estado:** Tabla de métricas actualizada tras cada interacción.

---

## 8. Supuestos y Restricciones
* **Supuesto:** El usuario posee conocimientos básicos de gestión de software para interpretar las métricas.
* **Restricción:** El sistema no almacena datos de usuario fuera de la sesión actual de simulación ( stateless por diseño en MVP).
* **Restricción de IA:** La calidad de la simulación depende del modelo de lenguaje subyacente (recomendado: modelos con alta capacidad de razonamiento lógico).

---
*Fin del Documento de Especificación.*