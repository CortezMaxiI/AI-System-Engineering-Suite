# State Transition Model
## Proyecto: DevTeam Sim – AI-Driven Development Team Simulator

**Versión:** 1.0  
**Fecha:** 22 de enero de 2026  
**Estado:** Modelo de Transición de Estado  
**Documentos Padre:** 01_SRS, 02_DESIGN_DECISIONS, 03_COGNITIVE_AGENTS  
**Propósito:** Definición del flujo causal de cambios en el vector de estado

---

## Preámbulo

El simulador opera como un sistema de transición de estados donde cada decisión del usuario genera consecuencias directas e indirectas sobre el vector de estado `S = {TD, M, R, P}`. Este documento define el modelo conceptual que gobierna dichas transiciones.

**Principio Fundamental:** El estado nunca cambia automáticamente. Todo cambio en `S` requiere un evento explícito: decisión del usuario, activación de evento latente, o inyección de entropía.

---

## 1. Ciclo de Simulación

El sistema opera en ciclos discretos. Cada ciclo sigue una secuencia invariante:

### 1.1 Secuencia del Ciclo

```
┌─────────────────────────────────────────────────────────────────┐
│  ESTADO ACTUAL (S_t)                                            │
│  Vector de métricas + Eventos latentes activos                  │
└─────────────────────┬───────────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────────┐
│  PRESENTACIÓN DE CONTEXTO                                       │
│  - Escenario o dilema técnico                                   │
│  - Estado visible del proyecto                                  │
│  - Eventos latentes a punto de activarse (si aplica)            │
└─────────────────────┬───────────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────────┐
│  DEBATE DE AGENTES                                              │
│  - Cada agente expone su postura según su función de utilidad   │
│  - El usuario puede interrogar con preguntas predefinidas       │
│  - Los agentes NO negocian entre sí                             │
└─────────────────────┬───────────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────────┐
│  DECISIÓN DEL USUARIO                                           │
│  - Selección entre opciones presentadas                         │
│  - Toda decisión implica trade-off (ver Sección 2)              │
└─────────────────────┬───────────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────────┐
│  FASE DE IMPACTO                                                │
│  1. Aplicación de impacto directo sobre S                       │
│  2. Generación de eventos latentes (si aplica)                  │
│  3. Evaluación de eventos latentes existentes                   │
│  4. Evaluación de inyección de entropía (según R)               │
│  5. Registro de trazabilidad                                    │
└─────────────────────┬───────────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────────┐
│  NUEVO ESTADO (S_t+1)                                           │
│  - Feedback estructurado al usuario                             │
│  - Inicio del siguiente ciclo                                   │
└─────────────────────────────────────────────────────────────────┘
```

### 1.2 Invariantes del Ciclo

- Un ciclo no puede completarse sin una decisión del usuario.
- El usuario no puede retroceder a un estado anterior.
- El sistema no avanza automáticamente sin intervención del usuario.

---

## 2. Principio de Trade-off Obligatorio

### 2.1 Definición

Toda decisión presentada al usuario debe cumplir la siguiente condición:

> **Si una decisión mejora al menos una métrica del vector S, debe empeorar al menos otra métrica del vector S.**

No existen decisiones "ganar-ganar" puras. El costo puede ser directo (inmediato) o diferido (evento latente).

### 2.2 Tipos de Trade-off

| Tipo | Descripción | Ejemplo |
|:-----|:------------|:--------|
| **Directo-Directo** | Mejora inmediata en una métrica, empeoramiento inmediato en otra | Lanzar sin tests: P↑, TD↑ |
| **Directo-Diferido** | Mejora inmediata, costo futuro mediante evento latente | Posponer refactor: P↑, genera evento latente "Acumulación Crítica" |
| **Diferido-Diferido** | Inversión ahora con beneficio y riesgo futuros | Refactor mayor: P↓ ahora, posible TD↓ futuro, posible M↓ si falla |

### 2.3 Decisiones Neutrales

En casos excepcionales, puede presentarse una decisión que no modifica métricas directamente, pero sí genera un evento latente o modifica la confianza de los agentes. Estas decisiones aún cumplen el principio: el costo existe, pero es cualitativo o diferido.

---

## 3. Impacto Directo

### 3.1 Definición

El impacto directo es la modificación inmediata del vector de estado `S` que ocurre tras una decisión del usuario, antes de evaluar eventos latentes o entropía.

### 3.2 Características

- **Determinista**: El impacto directo de una decisión específica es siempre el mismo.
- **Atómico**: Todas las modificaciones del impacto directo se aplican simultáneamente.
- **Acotado**: Los cambios respetan el rango [0, 100] de cada métrica.
- **Trazable**: Se registra la decisión como causa del cambio.

### 3.3 Métricas Afectadas por Tipo de Decisión

| Categoría de Decisión | Métricas Típicamente Afectadas |
|:----------------------|:-------------------------------|
| Decisiones de velocidad vs. calidad | P, TD |
| Decisiones de alcance | P, M |
| Decisiones de riesgo técnico | R, TD |
| Decisiones de gestión de equipo | M, P |

### 3.4 Comportamiento en Límites

- Si una métrica alcanza 0 o 100, el impacto que la excedería se trunca al límite.
- Alcanzar un límite puede generar un evento latente especial (ej. "Burnout del Equipo" si M = 0).

---

## 4. Eventos Latentes

### 4.1 Definición

Un evento latente es una consecuencia diferida de una decisión que no se manifiesta inmediatamente, sino que permanece "dormido" hasta cumplir ciertas condiciones.

### 4.2 Estructura de un Evento Latente

Cada evento latente tiene tres componentes:

| Componente | Descripción |
|:-----------|:------------|
| **Trigger** | Condición de activación basada en el estado actual del sistema |
| **Delay** | Número mínimo de ciclos antes de ser elegible para activación |
| **Payload** | Efecto sobre el vector S cuando se activa |

### 4.3 Ciclo de Vida

```
GENERACIÓN → LATENCIA → EVALUACIÓN → ACTIVACIÓN o DESCARTE
```

1. **Generación**: Una decisión del usuario crea el evento latente.
2. **Latencia**: El evento permanece inactivo durante su período de delay.
3. **Evaluación**: Una vez elegible, se evalúa el trigger cada ciclo.
4. **Resolución**:
   - Si el trigger se cumple: el evento se **activa** y aplica su payload.
   - Si el trigger no se cumple: el evento permanece latente.
   - Si condiciones alternativas lo invalidan: el evento se **descarta**.

### 4.4 Reglas de Eventos Latentes

- **Sin Encadenamiento**: Un evento latente no puede generar otro evento latente al activarse.
- **Visibilidad**: Los eventos latentes activos son visibles para el usuario en el reporte post-ciclo.
- **Límite por Sesión**: Existe un número máximo de eventos latentes simultáneos para prevenir complejidad excesiva.

### 4.5 Ejemplos Conceptuales de Eventos Latentes

| Evento | Generado Por | Trigger | Delay | Payload |
|:-------|:-------------|:--------|:------|:--------|
| Fuga de Talento | Ignorar al Tech Lead repetidamente | M < 40 | 2 ciclos | M↓, R↑ |
| Incidente en Producción | Lanzar sin tests | R > 60 | 1 ciclo | P↓, TD↑, M↓ |
| Acumulación Crítica | Posponer refactor | TD > 70 | 3 ciclos | Todas las decisiones técnicas tienen costo adicional |

---

## 5. Estocasticidad Controlada

### 5.1 Principio

El sistema no es determinista puro ni aleatorio puro. La estocasticidad existe únicamente en puntos controlados y está gobernada por el estado actual del sistema.

### 5.2 Elementos Deterministas

Los siguientes elementos producen siempre el mismo resultado dado el mismo estado:

| Elemento | Comportamiento |
|:---------|:---------------|
| Impacto directo de decisiones | Fijo para cada decisión |
| Generación de eventos latentes | Condiciones predefinidas |
| Evaluación de triggers | Comparación exacta contra umbrales |
| Comportamiento base de agentes | Definido por función de utilidad |

### 5.3 Elementos Estocásticos

Los siguientes elementos tienen variabilidad controlada:

| Elemento | Fuente de Variabilidad | Gobernado Por |
|:---------|:-----------------------|:--------------|
| Inyección de entropía | Evaluación probabilística por ciclo | Nivel actual de R + umbrales discretos |
| Tono de respuesta de agentes | Variación menor en lenguaje | Historial de confianza intra-sesión |
| Orden de argumentos en debate | Qué agente habla primero | Decisión anterior afectó más a quién |

### 5.4 Inyección de Entropía (detalle)

La inyección de entropía sigue el modelo de umbrales discretos definido en 02_DESIGN_DECISIONS.md:

| Nivel de R | Comportamiento |
|:-----------|:---------------|
| R < 30 | No se evalúa inyección |
| 30 ≤ R < 60 | Probabilidad baja de incidente |
| 60 ≤ R < 80 | Probabilidad media de incidente |
| R ≥ 80 | Probabilidad alta de incidente |

Cuando la inyección de entropía ocurre:
- Se selecciona un incidente del catálogo del escenario.
- El incidente tiene un impacto predefinido sobre S.
- El impacto se aplica después del impacto directo y los eventos latentes.

---

## 6. Trazabilidad

### 6.1 Principio

Todo cambio en el vector de estado debe ser atribuible a una causa específica identificable.

### 6.2 Causas Válidas de Cambio

| Tipo de Causa | Identificador | Ejemplo |
|:--------------|:--------------|:--------|
| Decisión del usuario | ID de decisión + ciclo | "D-03 en Ciclo 5" |
| Evento latente activado | ID del evento | "EL-02: Fuga de Talento" |
| Inyección de entropía | ID del incidente | "EN-01: Bug Crítico en Producción" |

### 6.3 Registro de Cambios

Cada modificación de métrica se registra con:

- **Métrica afectada**: TD, M, R, o P
- **Valor anterior**: Estado antes del cambio
- **Valor posterior**: Estado después del cambio
- **Delta**: Magnitud del cambio
- **Causa**: Identificador de la causa
- **Ciclo**: Momento en que ocurrió

### 6.4 Uso del Registro

- El reporte post-ciclo muestra el origen de cada delta.
- Al finalizar la sesión, el post-mortem puede reconstruir la cadena causal completa.
- El usuario puede consultar "¿por qué TD subió?" y obtener una respuesta determinista.

---

## 7. Flujo Completo con Ejemplo

A continuación se ilustra un ciclo completo con todos los componentes:

### Estado Inicial (S_t)
- TD: 35
- M: 65
- R: 45
- P: 40
- Eventos latentes activos: ninguno

### Contexto Presentado
"El Product Manager necesita lanzar la feature de pagos antes del viernes. El Tech Lead advierte que los tests de integración no están completos."

### Debate
- **Product Manager**: Argumenta urgencia comercial, tolerable incremento de deuda.
- **Tech Lead**: Señala riesgo de bugs en producción, propone retrasar.
- **Dev Pragmático**: Sugiere lanzar solo el flujo principal, tests parciales.

### Decisión del Usuario
"Lanzar con tests parciales, completar el resto post-lanzamiento."

### Fase de Impacto
1. **Impacto Directo**: P +15, TD +20, R +10
2. **Generación de Evento Latente**: "Deuda de Tests" (Trigger: TD > 60, Delay: 2 ciclos)
3. **Evaluación de Eventos Existentes**: No hay eventos latentes previos
4. **Evaluación de Entropía**: R = 55, dentro del rango bajo, no se inyecta incidente
5. **Registro**: Causa "D-01 Ciclo 1"

### Nuevo Estado (S_t+1)
- TD: 55
- M: 65
- R: 55
- P: 55
- Eventos latentes activos: "Deuda de Tests" (elegible en Ciclo 3)

---

## 8. Resumen de Invariantes del Modelo

| Invariante | Garantía |
|:-----------|:---------|
| El estado solo cambia por causas explícitas | Sin cambios automáticos ni ocultos |
| Toda decisión tiene trade-off | No existen opciones sin costo |
| Los eventos latentes no se encadenan | Complejidad acotada |
| La trazabilidad es completa | Todo delta tiene causa visible |
| La estocasticidad es controlada | Solo en puntos definidos y gobernada por el estado |

---

*Fin del Documento de Modelo de Transición de Estado.*
