using System.Text.Json.Serialization;

namespace TradeVision.DataBridge.Models
{
    // Usamos struct para stack allocation y evitar GC pressure en alta frecuencia
    public struct TradeEvent
    {
        [JsonPropertyName("e")]
        public string EventType { get; set; }

        [JsonPropertyName("E")]
        public long EventTime { get; set; }

        [JsonPropertyName("s")]
        public string Symbol { get; set; }

        [JsonPropertyName("t")]
        public long TradeId { get; set; }

        [JsonPropertyName("p")]
        public string Price { get; set; } // String para evitar precision loss antes de procesar

        [JsonPropertyName("q")]
        public string Quantity { get; set; }

        [JsonPropertyName("T")]
        public long TradeTime { get; set; }

        [JsonPropertyName("m")]
        public bool IsBuyerMaker { get; set; }
    }
}
