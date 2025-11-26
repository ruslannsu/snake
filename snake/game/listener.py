import threading
import socket

class GameListener(threading.Thread):

    def __init__(self, multicast_socket: socket.socket) -> None:
        super().__init__()
        self._multicast_socket = multicast_socket

    
    def start(self) -> None:
        return super().start()

    def run(self) -> None:
        while True:
            buf, addr = self._multicast_socket.recvfrom(1024)
            print(buf, addr)
            
    
    