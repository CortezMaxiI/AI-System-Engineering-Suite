using NetMQ;
using NetMQ.Sockets;
using TradeVision.DataBridge.Core;

namespace TradeVision.DataBridge
{
    class Program
    {
        private static PublisherSocket? _pubSocket;
        private static bool _running = true;

        static async Task Main(string[] args)
        {
            Console.Title = "TradeVision DataBridge (C# Core)";
            Log("SYSTEM", "Initializing OptiMax TradeVision DataBridge...");

            // 1. Setup ZeroMQ Publisher
            Log("ZMQ", "Binding Publisher to tcp://*:5555...");
            using (_pubSocket = new PublisherSocket())
            {
                _pubSocket.Bind("tcp://*:5555");
                Log("ZMQ", "Publisher Ready. Waiting for data...");

                // 2. Setup Binance Stream
                var binance = new BinanceStream(OnMarketDataReceived, msg => Log("BINANCE", msg));
                await binance.StartAsync();

                Log("SYSTEM", "Bridge is Active. Press CTRL+C to stop.");

                // 3. Keep Alive Loop
                // Prevent Main from exiting
                using (var cts = new CancellationTokenSource())
                {
                    Console.CancelKeyPress += (s, e) =>
                    {
                        e.Cancel = true;
                        _running = false;
                        cts.Cancel();
                        Log("SYSTEM", "Shutdown signal received.");
                    };

                    try
                    {
                        // Efficient wait
                        await Task.Delay(-1, cts.Token);
                    }
                    catch (TaskCanceledException)
                    {
                        // Graceful shutdown
                    }
                }

                await binance.StopAsync();
            }
            
            Log("SYSTEM", "Shutdown Complete.");
        }

        private static Task OnMarketDataReceived(string rawJson)
        {
            // In a high-freq scenario, we might want to deserialize here to validate 
            // OR just pass-through raw JSON to Python to save C# CPU cycles.
            // Given the requirement is "DataBridge", passing raw JSON is faster 
            // and lets Python handle the schema logic. 
            // HOWEVER, if we want "Luna Logic", maybe we parse to ensure validity?
            // Let's do Pass-Through for maximum speed (Zero Serialization Overhead in C#).
            
            // We publish with a topic.
            // Topic: "trade"
            _pubSocket?.SendMoreFrame("trade").SendFrame(rawJson);
            
            // Optional: Verbose log (Commented out for speed)
            // Log("STREAM", $"Relayed {rawJson.Length} bytes");

            return Task.CompletedTask;
        }

        private static void Log(string tag, string message)
        {
            var color = tag switch
            {
                "SYSTEM" => ConsoleColor.Cyan,
                "ZMQ" => ConsoleColor.Magenta,
                "BINANCE" => ConsoleColor.Yellow,
                "ERR" => ConsoleColor.Red,
                _ => ConsoleColor.White
            };

            Console.ForegroundColor = ConsoleColor.DarkGray;
            Console.Write($"[{DateTime.Now:HH:mm:ss}] ");
            Console.ForegroundColor = color;
            Console.Write($"[{tag}] ");
            Console.ForegroundColor = ConsoleColor.Gray;
            Console.WriteLine(message);
        }
    }
}
