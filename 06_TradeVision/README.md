👁️ OptiMax TradeVision: Agentic Financial Module v2.1
TradeVision es un sistema híbrido de análisis y trading de alta frecuencia diseñado para el ecosistema OptiMax. Separa el "Músculo" (C#) del "Cerebro" (Python), logrando una ejecución de baja latencia con razonamiento agéntico avanzado.

🏗️ Arquitectura de Alto Nivel
TradeVision utiliza una arquitectura desacoplada mediante un Neural Link (ZeroMQ), garantizando máximo rendimiento y modularidad.
🦾 El Músculo: TradeVision.DataBridge (C#)
Rol: Ingestión de datos en tiempo real desde el WebSocket de Binance.
Lógica: Basado en Luna Predator. Usa System.Net.WebSockets para una conexión asíncrona de alto flujo.
ZeroMQ PUB: Actúa como Publisher, enviando datos crudos a un socket IPC (tcp://127.0.0.1:5555).
🧠 El Cerebro: TradeAnalystAgent (Python)
Rol: Toma de decisiones agéntica y procesamiento de señales.
Arquitectura de Capas (v2.1): Procesa el flujo de datos mediante un motor de consenso de tres niveles.

🔬 Motor de Consenso (Three-Layer Engine)
A diferencia de los bots simples, TradeVision v2.1 utiliza una Arquitectura de Confluencia Real para eliminar señales falsas:
Capa 1: Análisis Técnico Pro: Calcula RSI (14) y EMAs (20/200) para detectar tendencias y zonas de agotamiento.
Capa 2: Inteligencia de Noticias (Real-time): Conectada a la API de CryptoPanic. El agente escanea titulares globales en tiempo real buscando eventos macro (ETFs, Hacks, Fed).
Capa 3: Filtro de Riesgo (News-Lock): * Si la técnica dice "BUY" pero el sentimiento es NEGATIVO, el agente bloquea la operación.
Incluye el titular de la noticia relevante en la alerta final para total transparencia.

🛠️ Stack Tecnológico
Componente
Tecnología
Ingestion Core
.NET 8.0 / C#
IPC Link
NetMQ / pyzmq (ZeroMQ)
Reasoning Engine
Python 3.11+ (Pandas-TA)
News Intelligence
CryptoPanic API (Real-time)
Persistence
Supabase (PostgreSQL)
Alerts
Telegram Bot API (Español)


🚀 Guía Operativa
📋 Requisitos Previos
.NET 8.0 SDK.
Python 3.11+ con dependencias: pip install pandas pandas-ta requests pyzmq.
Variables de Entorno (.env):
Fragmento de código
SUPABASE_URL=tu_url
SUPABASE_KEY=tu_key
TELEGRAM_TOKEN=tu_token
TELEGRAM_CHAT_ID=tu_id
CRYPTOPANIC_TOKEN=tu_token_real



📊 Observabilidad y Persistencia
Cada decisión se guarda en Supabase e incluye:
Signal: BUY / SELL / HOLD.
Confidence: Fuerza del consenso (0% - 100%).
Reasoning: Explicación humana (Ej: "RSI 30 + News Sentiment Positivo (ETF Approval)").
Telegram: Notificaciones detalladas en español con el titular de la noticia que influyó en el trade.

Optimax Suite - TradeVision Module v2.1 (News Intelligence Active)
