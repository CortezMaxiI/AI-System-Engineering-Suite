import zmq
import json
import time
from typing import Callable, Any

class ZMQSubscriber:
    def __init__(self, topic: str = "trade", host: str = "tcp://127.0.0.1:5555"):
        self.host = host
        self.topic = topic
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.SUB)
        self.running = False

    def start(self, callback: Callable[[dict], None]):
        """
        Starts the subscriber loop.
        callback: Function to handle deserialized data.
        """
        print(f"[\033[96mNET\033[0m] Connecting to Neural Link at {self.host}...")
        try:
            self.socket.connect(self.host)
            self.socket.setsockopt_string(zmq.SUBSCRIBE, self.topic)
            self.running = True
            
            print(f"[\033[96mNET\033[0m] Link Established. Listening for '{self.topic}' events.")
            
            while self.running:
                try:
                    # Receive multipart: [topic, message]
                    if self.socket.poll(100): # Non-blocking check every 100ms
                        topic_bytes, msg_bytes = self.socket.recv_multipart()
                        
                        # Decode
                        topic = topic_bytes.decode('utf-8')
                        raw_json = msg_bytes.decode('utf-8')
                        
                        try:
                            data = json.loads(raw_json)
                            callback(data)
                        except json.JSONDecodeError:
                            print(f"[\033[91mERR\033[0m] Malformed JSON received on connector.")
                            
                except zmq.ZMQError as e:
                    print(f"[\033[91mERR\033[0m] ZMQ Error: {e}. Reconnecting...")
                    self._reconnect()
                    
        except KeyboardInterrupt:
            print("\n[\033[96mNET\033[0m] Disconnecting...")
        finally:
            self.socket.close()
            self.context.term()

    def _reconnect(self):
        self.socket.close()
        time.sleep(1)
        self.socket = self.context.socket(zmq.SUB)
        self.socket.connect(self.host)
        self.socket.setsockopt_string(zmq.SUBSCRIBE, self.topic)
