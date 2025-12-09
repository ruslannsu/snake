import threading
import socket
import time
from proto.proto_messages import ProtoMessages

class GameSender(threading.Thread):

    def __init__(self, multicast_socket: socket.socket) -> None:
        super().__init__()
        self._multicast_socket = multicast_socket
        self._proto_messages = ProtoMessages()
        self._message = None

    def start(self) -> None:
        return super().start()

    def run(self) -> None:
        while True:
            time.sleep(2)
            if self._message is None: 
                continue

            self._multicast_socket.sendto(self._message, ('239.192.0.4', 9192))
            
            

            
    