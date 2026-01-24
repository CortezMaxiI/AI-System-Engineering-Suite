# Project: OptiMax TradeVision (Agentic Financial Module)

## 1. Objetivo General
Desarrollar un sistema agéntico de trading que integre el procesamiento de datos de alta frecuencia (Luna Predator logic) con la toma de decisiones basada en razonamiento de IA (EA Engine logic).

## 2. Requerimientos Funcionales
- **Data Ingestion (C# Core):** El sistema debe extraer datos en tiempo real de la API de Binance (par BTC/USDT) utilizando una arquitectura de baja latencia inspirada en Luna Predator.
- **Agentic Analysis (Python Core):** El agente debe procesar los datos recibidos y actuar bajo un consenso de dos capas:
    1. Capa Técnica: Análisis de indicadores (RSI, Medias Móviles).
    2. Capa Fundamental: Análisis de sentimiento de noticias/redes mediante el motor de IA.
- **Decision Engine:** El sistema no solo debe alertar, sino generar una recomendación de acción estructurada (BUY/SELL/HOLD) con su respectiva justificación (Reasoning).
- **Persistence:** Registro de logs, decisiones y estados del mercado en la base de datos Supabase existente.

## 3. Integración
- El módulo debe ser capaz de enviar señales de estado a la interfaz OptiMax Web (Luna).