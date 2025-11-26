import threading
import socket
import time

class GameSender(threading.Thread):

    def __init__(self, multicast_socket: socket.socket) -> None:
        super().__init__()
        self._multicast_socket = multicast_socket

    
    def start(self) -> None:
        return super().start()

    def run(self) -> None:
        while True:
            self._multicast_socket.sendto(b'123', ('239.192.0.4', 9192))
            time.sleep(2)
            

            
    