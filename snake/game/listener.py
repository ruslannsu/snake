import threading
import socket
from collections import deque
import time
from event_bus.event_bus import event_bus
from proto.proto_messages import ProtoMessages
time.time()

class GameListener(threading.Thread):
    def __init__(self, multicast_socket: socket.socket) -> None:
        super().__init__()
        self._multicast_socket = multicast_socket
        self._messages = []
        self._proto_messages = ProtoMessages()
        
    @property
    def messages(self):
        return self._messages
    
    def start(self) -> None:
        return super().start()

   
    def run(self) -> None:
        time_point = time.time()
        while True:
            
            if time.time() - time_point > 5:
                time_point = time.time()
                self._messages.clear()
            
            buf, addr = self._multicast_socket.recvfrom(1024)
            print(addr)
            self._messages.append(self._proto_messages.deserialize(buf))
            time.sleep(1)
            event_bus.notify(event_name='get_announcement')
            
            
            print(buf, addr)
            
    
    