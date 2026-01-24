# Design Decisions Document
## Proyecto: DevTeam Sim – AI-Driven Development Team Simulator

**Versión:** 1.0  
**Fecha:** 22 de enero de 2026  
**Estado:** Decisiones de Diseño Aprobadas  
**Documento Padre:** 01_SRS_DevTeam_Sim.md  
**Propósito:** Resolución explícita de ambigüedades identificadas en auditoría

---

## Preámbulo

Este documento complementa al SRS y resuelve las ambigüedades detectadas durante la auditoría de diseño. Las decisiones aquí documentadas priorizan:

1. **Simplicidad**: Evitar complejidad innecesaria en el MVP.
2. **Coherencia Sistémica**: Mantener alineación con los principios de fricción, trade-offs y causalidad.
3. **Control del Crecimiento**: Prevenir explosión de variables o estados inmanejables.

---

## Resolución de Ambigüedades

---

### A-01: Rangos del Vector de Estado

**Decisión:**  
Las cuatro métricas del vector de estado `S_t = {TD, M, R, P}` operan en el rango cerrado **[0, 100]**.

**Justificación Sistémica:**  
Un dominio acotado permite comparaciones intuitivas, previene divergencia infinita y facilita la calibración de umbrales de eventos latentes.

**Impacto Esperado:**  
Las métricas tendrán comportamiento predecible. Los valores extremos (0 o 100) representarán puntos de inflexión narrativos en la simulación.

---

### A-02: "Confianza en el liderazgo" (RF-03)

**Decisión:**  
La confianza en el liderazgo **no es una variable separada**. Se modela como un modificador interno de cada agente que afecta su disposición a aceptar decisiones del usuario. Este modificador se deriva directamente de la métrica global `M` (Moral) y del historial de decisiones que contradicen la postura del agente.

**Justificación Sistémica:**  
Introducir una quinta métrica rompería la simplicidad del vector `S_t`. El comportamiento de "desconfianza" puede simularse con reglas cualitativas sin expandir el modelo cuantitativo.

**Impacto Esperado:**  
Los agentes cuya postura fue ignorada repetidamente mostrarán resistencia creciente en debates futuros, sin requerir una variable adicional.

---

### A-03: Definición de "Evento Latente"

**Decisión:**  
Un Evento Latente es una **consecuencia diferida** de una decisión, definida por:
- **Trigger**: Condición de activación (ej. `TD > 70`, `M < 30`).
- **Delay**: Número de ciclos antes de que el evento sea elegible para activación.
- **Payload**: Efecto sobre el vector de estado cuando se activa.

Los eventos latentes **no se encadenan**. Un evento latente puede modificar `S_t`, pero no puede generar nuevos eventos latentes.

**Justificación Sistémica:**  
Prohibir el encadenamiento previene explosión combinatoria y mantiene la trazabilidad causal lineal.

**Impacto Esperado:**  
El sistema tendrá consecuencias diferidas predecibles. El usuario podrá anticipar riesgos sin enfrentar cascadas impredecibles.

---

### A-04: Disparo de eventos por `R` (RF-06)

**Decisión:**  
La inyección de entropía se evalúa una vez por ciclo de decisión mediante un **sistema de umbrales discretos**, no una función continua:

| Nivel de R | Probabilidad de Incidente |
|:-----------|:--------------------------|
| R < 30     | Sin incidentes            |
| 30 ≤ R < 60| Baja                      |
| 60 ≤ R < 80| Media                     |
| R ≥ 80     | Alta                      |

Las probabilidades exactas (Baja, Media, Alta) se definirán en la especificación del motor.

**Justificación Sistémica:**  
Umbrales discretos son más intuitivos para el usuario y más fáciles de calibrar que funciones continuas.

**Impacto Esperado:**  
El usuario percibirá bandas de riesgo claras. La tensión narrativa aumentará al acercarse a umbrales conocidos.

---

### A-05: Interacción entre métricas

**Decisión:**  
Las métricas del vector de estado **no tienen dependencias automáticas entre sí**. Toda modificación de una métrica requiere un evento explícito (decisión del usuario, evento latente, inyección de entropía).

**Justificación Sistémica:**  
Evitar acoplamientos ocultos garantiza trazabilidad completa y previene comportamientos emergentes no diseñados.

**Impacto Esperado:**  
Cada cambio en `S_t` será atribuible a una causa específica. El post-mortem de simulación será determinista.

---

### A-06: QA Engineer en MVP

**Decisión:**  
El MVP incluirá **únicamente 3 agentes** según la Sección 7 del SRS: Tech Lead, Product Manager y Developer Pragmático. El QA Engineer queda **diferido a una versión posterior**.

**Justificación Sistémica:**  
Los 3 agentes del MVP ya representan el conflicto triangular fundamental (calidad vs. velocidad vs. simplicidad). El QA agrega complejidad sin cambiar la dinámica central.

**Impacto Esperado:**  
El MVP será más fácil de calibrar. La visibilidad del riesgo (`R`) será responsabilidad compartida de los agentes existentes, no de un rol especializado.

---

### A-07: "Interrogar a los agentes" (UC-01.3)

**Decisión:**  
La interrogación a agentes se realiza mediante un **catálogo finito de preguntas predefinidas** por tipo de escenario, no mediante diálogo libre.

Ejemplos de preguntas:
- "¿Cuáles son los riesgos de esta opción?"
- "¿Cómo afectará esto al equipo?"
- "¿Qué precedente establece esta decisión?"

**Justificación Sistémica:**  
Las preguntas predefinidas garantizan coherencia de rol (RNF-01) y evitan que el usuario extraiga respuestas fuera del marco de la simulación.

**Impacto Esperado:**  
La interacción será estructurada y replicable. Los agentes no podrán ser "manipulados" hacia posturas inconsistentes.

---

### A-08: "Feedback estructurado" (RF-05)

**Decisión:**  
El reporte post-ciclo incluirá:
1. **Vector de Estado Actualizado** (`S_t`).
2. **Delta de Métricas** (cambio respecto al ciclo anterior).
3. **Eventos Latentes Activos** (lista con triggers visibles).
4. **Origen de Cambios** (referencia a la decisión o evento que causó cada delta).

No incluirá gráficos, predicciones ni análisis narrativo automatizado.

**Justificación Sistémica:**  
Un reporte tabular y factual cumple RNF-02 (Trazabilidad) sin requerir generación de lenguaje natural adicional.

**Impacto Esperado:**  
El usuario tendrá visibilidad clara del impacto de cada decisión. La interpretación del estado queda bajo responsabilidad del usuario.

---

### A-09: Moral Global vs. Moral por Agente

**Decisión:**  
`M` es una **métrica global** que representa el estado emocional agregado del equipo. Los agentes individuales **no tienen una métrica de moral separada**.

Cuando una decisión afecta desproporcionadamente a un agente (ej. ignorar al Tech Lead), el impacto se refleja en:
1. Reducción del `M` global.
2. Modificador cualitativo en el comportamiento del agente afectado (ver A-02).

**Justificación Sistémica:**  
Una sola métrica de moral simplifica el modelo y es suficiente para el MVP. La diferenciación por agente puede agregarse en versiones futuras sin romper el modelo base.

**Impacto Esperado:**  
El usuario gestionará la moral del equipo como un recurso colectivo, no como N variables individuales.

---

### A-10: "Stateless por diseño en MVP"

**Decisión:**  
El sistema es stateless **entre sesiones**, pero mantiene estado completo **dentro de una sesión**. La Persistencia Cognitiva (RF-03) opera exclusivamente durante la sesión activa.

Definición de sesión: desde que el usuario inicia un escenario hasta que lo finaliza o abandona.

**Justificación Sistémica:**  
Esto cumple tanto con el requerimiento de memoria persistente de agentes como con la restricción de no almacenar datos de usuario.

**Impacto Esperado:**  
Cada partida es un experimento aislado. Los agentes recordarán decisiones dentro de la sesión, pero no entre sesiones diferentes.

---

## Resumen de Decisiones

| ID | Decisión Clave |
|:---|:---------------|
| A-01 | Métricas en rango [0, 100] |
| A-02 | Confianza derivada de M + historial, no es variable separada |
| A-03 | Eventos latentes no encadenables |
| A-04 | Entropía por umbrales discretos |
| A-05 | Sin dependencias automáticas entre métricas |
| A-06 | QA diferido, MVP con 3 agentes |
| A-07 | Interrogación mediante preguntas predefinidas |
| A-08 | Reporte tabular sin análisis narrativo |
| A-09 | Moral global, no individual |
| A-10 | Stateless entre sesiones, stateful dentro de sesión |

---

*Fin del Documento de Decisiones de Diseño.*
