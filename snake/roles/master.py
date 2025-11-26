from threading import Thread
from snake.roles.base import BaseRole
import socket

from uuid import UUID

class Master(BaseRole):
    def __init__(self, multicast_socket: socket.socket, multicast_group: tuple, id: UUID) -> None:
        super().__init__(multicast_socket=multicast_socket, id=id)
        self._multicast_group = multicast_group

    def _send_game_anouncment(self):
        self._multicast_socket.sendto(b"1234", self._multicast_group)

    def run(self) -> None:
        pass
        
        
        