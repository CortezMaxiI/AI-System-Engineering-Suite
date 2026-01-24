using System.Net.WebSockets;
using System.Text;

namespace TradeVision.DataBridge.Core
{
    public class BinanceStream
    {
        private const string BINANCE_WS_URL = "wss://stream.binance.com:9443/ws/btcusdt@trade";
        private ClientWebSocket _ws;
        private readonly CancellationTokenSource _cts;
        private readonly Func<string, Task> _onMessage;
        private readonly Action<string> _logger;

        public BinanceStream(Func<string, Task> onMessage, Action<string> logger)
        {
            _ws = new ClientWebSocket();
            _cts = new CancellationTokenSource();
            _onMessage = onMessage;
            _logger = logger;
        }

        public async Task StartAsync()
        {
            try
            {
                _logger($"[NET] Connecting to {BINANCE_WS_URL}...");
                await _ws.ConnectAsync(new Uri(BINANCE_WS_URL), _cts.Token);
                _logger("[NET] Connected to Binance Stream.");

                _ = ReceiveLoop();
            }
            catch (Exception ex)
            {
                _logger($"[ERR] Connection failed: {ex.Message}");
            }
        }

        private async Task ReceiveLoop()
        {
            var buffer = new byte[8192]; // 8KB buffer
            
            while (_ws.State == WebSocketState.Open && !_cts.Token.IsCancellationRequested)
            {
                try
                {
                    // Memory<T> is better for zero allocation slicing if we wanted to go deep, 
                    // but ArraySegment is standard enough here.
                    var result = await _ws.ReceiveAsync(new ArraySegment<byte>(buffer), _cts.Token);

                    if (result.MessageType == WebSocketMessageType.Close)
                    {
                        _logger("[NET] Binance server requested close.");
                        await _ws.CloseAsync(WebSocketCloseStatus.NormalClosure, "Closing", CancellationToken.None);
                        break;
                    }

                    if (result.Count > 0)
                    {
                        var json = Encoding.UTF8.GetString(buffer, 0, result.Count);
                        await _onMessage(json);
                    }
                }
                catch (Exception ex)
                {
                    _logger($"[ERR] WebSocket Error: {ex.Message}");
                    // Simple reconnect logic could go here
                    await Task.Delay(5000);
                    // Reconnect logic... (omitted for MVP brevity, but crucial for Prod)
                }
            }
        }

        public async Task StopAsync()
        {
            _cts.Cancel();
            if (_ws.State == WebSocketState.Open)
                await _ws.CloseAsync(WebSocketCloseStatus.NormalClosure, "Stop", CancellationToken.None);
            _ws.Dispose();
        }
    }
}
