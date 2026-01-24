-- Table Definition for TradeVision Persistence
-- Run this in the Supabase SQL Editor

CREATE TABLE IF NOT EXISTS trade_logs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    timestamp TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    symbol TEXT NOT NULL,
    price NUMERIC NOT NULL,
    signal TEXT NOT NULL,
    confidence NUMERIC NOT NULL,
    reasoning TEXT
);

-- Optional: Index for faster queries on symbol and time
CREATE INDEX IF NOT EXISTS idx_trade_logs_symbol_time ON trade_logs (symbol, timestamp DESC);
