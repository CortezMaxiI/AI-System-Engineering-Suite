# Sentinel-IIoT: Predictive Lumi Engine

![Status](https://img.shields.io/badge/Status-Production--Ready-blueviolet?style=for-the-badge)
![Version](https://img.shields.io/badge/Version-1.0.0-purple?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**Sentinel-IIoT** es un motor de análisis agéntico diseñado para el monitoreo industrial crítico. Utilizando una arquitectura desacoplada de alto rendimiento, el sistema transforma la telemetría bruta de sensores en inteligencia accionable, detectando anomalías antes de que se conviertan en fallos costosos y optimizando la vida útil de los activos industriales.

---

## 👁️ Visual Showcase
![Sentinel-IIoT Dashboard](assets/screenshot.gif)
*Lumi Engine HUD: Monitoreo en tiempo real con Gemelo Digital reactivo.*

---

## 🔮 ¿Qué es Sentinel-IIoT?
En el corazón de la Industria 4.0, **Sentinel-IIoT** redefine el mantenimiento predictivo mediante el uso de **Agentes Inteligentes**. A diferencia de los sistemas de monitoreo pasivo, Sentinel opera bajo la filosofía de "Predictive Lumi", donde cada bit de dato es analizado por un "Cerebro" de IA capaz de proyectar ventanas de fallo y niveles de degradación con alta precisión.

### El Desafío Industrial
Las paradas no programadas cuestan a la industria millones de dólares anualmente. Sentinel-IIoT soluciona esto mediante:
*   **Mantenimiento Predictivo Agéntico:** Decisiones basadas en modelos de datos, no en simples umbrales.
*   **Integración IIoT Nativa:** Conexión sin fisuras entre el hardware (Muscle) y la lógica de decisión (Brain).
*   **Gobernanza de Datos:** Trazabilidad completa de cada diagnóstico para auditorías de seguridad.

---

## 🏗️ Arquitectura del Sistema: The Neural Link
Sentinel-IIoT implementa una arquitectura **Brain (Python) ↔ Muscle (C#)**, conectada mediante un enlace neuronal de baja latencia utilizando **ZeroMQ**.

1.  **The Muscle (C# / .NET 8):** El motor ejecutivo. Encargado de capturar telemetría, persistir datos en la nube y ejecutar acciones inmediatas.
2.  **The Brain (Python 3.11):** El núcleo de razonamiento. Analiza tendencias de vibración, temperatura y carga eléctrica para emitir diagnósticos predictivos.
3.  **Lumi HUD (WPF):** La interfaz de mando. Un HUD industrial futurista que visualiza el estado de salud mediante un Gemelo Digital vibrante.

---

## 🚀 Características Principales

### 📊 Monitoreo en Tiempo Real
Visualización instantánea de métricas críticas industriales:
*   **Vibración (G-force):** Análisis de ondas para detección de desalineación o desgaste.
*   **Temperatura (°C):** Control térmico de componentes críticos.
*   **Amperaje/Carga (A):** Monitoreo de eficiencia eléctrica y sobreesfuerzo motor.

### 🧠 Inteligencia Agéntica
*   **Health Score (0-100):** Indicador holístico de la salud del activo.
*   **Status Dinámico:** Estados de operación *OPTIMAL*, *DEGRADED* y *CRITICAL*.
*   **RUL (Remaining Useful Life):** Predicción de ventana de fallo en horas/días.

### 🛡️ Gobernanza y Seguridad (Safety Gate)
*   **Audit Trail:** Generación automática de UUIDs para cada evento crítico.
*   **Confidence Score:** Cada decisión de la IA incluye un porcentaje de confianza científica.
*   **Telemetry Snapshot:** Captura del estado exacto de los sensores al momento de un incidente.
*   **Alertas Multi-canal:** Integración con Telegram Bot para notificaciones de alta criticidad (>90% confianza).

### 🎨 UX Lumi V3
*   **Gemelo Digital Reactivo:** Un núcleo central que cambia de gradiente y pulso según la salud de la máquina.
*   **Modo Resiliente:** El HUD sigue operando y visualizando datos locales incluso si falla la conexión a la base de datos o la IA externa.

---

## 🛠️ Tecnologías Utilizadas

*   **Backend Ejecutivo:** .NET 8 (C#) con NetMQ & HandyControl.
*   **Motor de IA:** Python 3.11 con pyzmq & Pydantic.
*   **Visualización:** WPF (Windows Presentation Foundation) con ADN estético Lumi V3.
*   **Conectividad:** ZeroMQ (PUB/SUB & REQ/REP).
*   **Persistencia:** Supabase (PostgreSQL / Realtime).
*   **Comunicaciones:** Telegram Bot API.

---

## 🏁 Cómo Ejecutar el Proyecto

### 1. Requisitos Previos
*   .NET 8 SDK
*   Python 3.11+
*   Cuenta en Supabase y Token de Telegram (opcional para alertas).

### 2. Configuración de Variables de Entorno
Crea o configura las siguientes variables en tu sistema:
```bash
SUPABASE_URL="tu_url_de_supabase"
SUPABASE_KEY="tu_anon_key"
TELEGRAM_TOKEN="tu_bot_token"
TELEGRAM_CHAT_ID="tu_chat_id"
```

### 3. Orden de Inicio
Para que el Neural Link se establezca correctamente, inicia los módulos en este orden:

1.  **Inicia el Muscle (Telemetría):**
    ```powershell
    cd Sentinel-Muscle-CS
    dotnet run
    ```
2.  **Inicia el Brain (Análisis AI):**
    ```powershell
    cd Sentinel-Brain-PY
    python main.py
    ```
3.  **Inicia el HUD (Visualización):**
    ```powershell
    cd Sentinel-UI-WPF
    dotnet run
    ```

---

## 🤝 Contribuciones
¡Las contribuciones son bienvenidas! Si tienes ideas para nuevos sensores, modelos de predicción o mejoras estéticas, siéntete libre de abrir un Pull Request.

---

## 📜 Licencia
Este proyecto está bajo la licencia **MIT**. Consulta el archivo `LICENSE` para más detalles.

---
*Desarrollado bajo el estándar de excelencia Lumi V3.* 🌌
