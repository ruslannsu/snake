import socket
from snake.roles.base import BaseRole
import struct
from ui.controller.controller import Controller
from ui.view.view import View
from ui.model.model import Model
class Game:
    def __init__(self) -> None:
        self._unicast_socket = self._create_unicast_socket()
        self._id = '43'
        self._role = None
        self._multicast_group = ('a1', 1)
    
        self._view = View()
        self._model = Model()

        self._controller = Controller(view=self._view, model=self._model)

        
    
    def _create_unicast_socket(self):
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        udp_socket.bind(('', self._multicast_group[1]))
        mreq = struct.pack("4s4s", socket.inet_aton(self._multicast_group[0]), socket.inet_aton('0.0.0.0'))
        udp_socket.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
        
       
        udp_socket.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)
        
        return udp_socket
    
  