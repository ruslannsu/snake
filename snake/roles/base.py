import socket

class BaseRole:
    def __init__(self, id: str, multicast_socket: socket.socket) -> None:
        self._id = id
        self._multicast_socket = multicast_socket
        
        
    