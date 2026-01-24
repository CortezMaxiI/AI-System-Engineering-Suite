Documento de Especificación de Requerimientos (ERS) - Proyecto Guardian
documento de especificacion de requeremientosVersión: 1.0

Estado: Definición Conceptual

Propósito: Actuar como primer respondiente inteligente ante fallos de infraestructura, priorizando la seguridad y la supervisión humana.

1. Descripción General del Sistema
Guardian es un middleware de observabilidad activa que integra Inteligencia Artificial para diagnosticar fallos en tiempo real. Su objetivo no es la automatización ciega, sino el cierre de la brecha entre la detección de un error y la intervención humana calificada, proporcionando contexto, simulaciones de mitigación y propuestas de acción validadas.

2. Requerimientos Funcionales (RF)
RF1: Ingesta y Monitoreo Multifuente: El sistema debe conectarse a streams de logs, métricas y trazas (APIs, Prometheus, CloudWatch, etc.).

RF2: Motor de Diagnóstico (Razonamiento): Capacidad de analizar anomalías y correlacionar eventos históricos para generar una hipótesis de causa raíz.

RF3: Entorno de Simulación (Sandboxing): El sistema debe contar con un entorno aislado (ej. contenedores efímeros) para probar scripts de mitigación antes de proponerlos.

RF4: Gestión de Decisiones (Triaje):

Clasificar acciones en: Segura (ejecución sugerida), Riesgosa (requiere aprobación), Peligrosa (bloqueada/rechazada).

RF5: Interfaz de Comunicación Humano-IA: Un panel de control o bot de comando donde Guardian presente: Problema -> Evidencia -> Simulación -> Propuesta.

RF6: Trazabilidad y Memoria: Registro inmutable de cada razonamiento y resultado de acción para auditoría y aprendizaje del sistema.

3. Requerimientos No Funcionales (RNF)
RNF1: Seguridad (Principio de Menor Privilegio): Guardian no tendrá acceso de escritura total a la infraestructura de producción sin intermediarios de validación.

RNF2: Disponibilidad: El sistema debe operar de forma independiente a los servicios que monitorea (aislamiento de falla).

RNF3: Latencia: El diagnóstico inicial debe entregarse en < 60 segundos tras la detección de la anomalía.

RNF4: Honestidad Intelectual: El sistema debe declarar explícitamente cuando no tiene suficiente información para actuar o diagnosticar.