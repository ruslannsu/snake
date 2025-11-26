import socket
from snake.roles.master import Master
import struct
from ui.controller.controller import Controller
from ui.view.view import View
from ui.model.model import Model
from snake.game.listener import GameListener
import threading
import uuid

class Game:
    def __init__(self) -> None:
        self._id = uuid.uuid4()
        print(self._id)
        self._role = None

        multicast_group = ('239.192.0.4', 9192)
        
        self._multicast_socket = self._create_multicast_socket(multicast_group=multicast_group)

        game_listener = GameListener(multicast_socket=self._multicast_socket)
        game_listener.start()

        self._view = View()
        self._model = Model()

        self._master_role = Master(multicast_socket=self._multicast_socket, id=self._id, multicast_group=multicast_group)
        self._controller = Controller(view=self._view, model=self._model, master_role=self._master_role)
    
    def _create_multicast_socket(self, multicast_group):
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        udp_socket.bind(('', multicast_group[1]))
        print(udp_socket.getsockname())

        mreq = struct.pack("4s4s", socket.inet_aton(multicast_group[0]), socket.inet_aton('0.0.0.0'))

        udp_socket.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
        udp_socket.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)

        return udp_socket