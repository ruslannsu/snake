from threading import Thread
from snake.roles.base import BaseRole
import socket
from proto import snakes_pb2

class Master(BaseRole):
    def __init__(self, multicast_socket: socket.socket, id: str) -> None:
        super().__init__(multicast_socket=multicast_socket, id=id)
        
        

    def _send_game_anouncment(self):
        pass

    def run(self) -> None:
        pass
        
        
        