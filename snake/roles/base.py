import socket
from uuid import UUID
class BaseRole:
    def __init__(self, id: UUID, multicast_socket: socket.socket) -> None:
        self._id = id
        self._multicast_socket = multicast_socket
        
        
    