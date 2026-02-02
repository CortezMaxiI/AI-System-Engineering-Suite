👁️ OptiMax TradeVision — Agentic Financial Module v2.1
TradeVision is a hybrid high-frequency analysis and trading system designed for the OptiMax ecosystem.
 It enforces a strict separation between execution (Muscle) and reasoning (Brain), enabling low-latency operation combined with advanced agentic decision-making.

🏗️ High-Level Architecture
TradeVision is built on a fully decoupled architecture using a Neural Link (ZeroMQ) to maximize performance, modularity, and fault isolation.

🦾 The Muscle — TradeVision.DataBridge (C# / .NET 8)
Role:
 Real-time market data ingestion from Binance WebSocket feeds.
Details:
Asynchronous, high-throughput pipeline based on Luna Predator principles


Uses System.Net.WebSockets for low-latency streaming


Publishes raw tick data via ZeroMQ PUB over IPC
 (tcp://127.0.0.1:5555)



🧠 The Brain — TradeAnalystAgent (Python)
Role:
 Agentic reasoning, signal processing, and decision validation.
v2.1 Layered Architecture:
 Market data is processed through a three-layer consensus engine designed to eliminate false positives and prevent blind automation.

🔬 Three-Layer Consensus Engine
Unlike conventional bots, TradeVision v2.1 implements Real Confluence Architecture:
Layer 1 — Advanced Technical Analysis
RSI (14)


EMA (20 / 200)


Trend detection and exhaustion zones


Layer 2 — Real-Time News Intelligence
Live integration with CryptoPanic API


Continuous scanning of global macro events
 (ETFs, exploits, regulatory actions, central banks)


Layer 3 — Risk Filter (News-Lock)
If technical signals indicate BUY but news sentiment is negative, execution is blocked


The triggering news headline is attached to the final alert for full transparency



🛠️ Technology Stack
Execution Core: .NET 8 / C#


IPC: NetMQ / pyzmq (ZeroMQ)


Reasoning Engine: Python 3.11+ (Pandas-TA)


News Intelligence: CryptoPanic API (real-time)


Persistence: Supabase (PostgreSQL)


Alerts: Telegram Bot API (Spanish)



📊 Observability & Traceability
Every decision is persisted and auditable, including:
Signal: BUY / SELL / HOLD


Confidence: Consensus strength (0–100%)


Reasoning: Human-readable explanation
 (e.g., “RSI 30 + Positive ETF-related News Sentiment”)



⚠️ Engineering Philosophy
Execution is never blind


Risk awareness > raw speed


Every action must be explainable, traceable, and reviewable




Telegram: Notificaciones detalladas en español con el titular de la noticia que influyó en el trade.

Optimax Suite - TradeVision Module v2.1 (News Intelligence Active)

