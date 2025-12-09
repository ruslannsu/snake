import socket
import struct
from ui.controller.controller import Controller
from ui.view.view import View
from ui.model.model import Model
from snake.game.listener import GameListener
from snake.game.sender import GameSender
from snake.game.game_config import GameConfig
import threading
import uuid
import yaml

class Game:
    def __init__(self) -> None:
        self._id = uuid.uuid4()
        self._role = None

        self._config = self._load_config()

        self._field_width = self._config['game_params']['game_field_width'] 
        self._field_height = self._config['game_params']['game_field_height'] 
        self._food_static = self._config['game_params']['food_static']
        self._delay = self._config['game_params']['delay']
        self._sidebar_width = self._config['game_params']['sidebar_width']
        self._grid_size = self._config['game_params']['grid_size']


        self._game_config = GameConfig(field_height=self._config['game_params']['game_field_width'],
                                        food_static=self._config['game_params']['food_static'],
                                          delay=self._config['game_params']['delay'],
                                            field_width= self._config['game_params']['game_field_width'],
                                            sidebar_width=self._sidebar_width, grid_size=self._grid_size)

        multicast_group = ('239.192.0.4', 9192)
        self._multicast_socket = self._create_multicast_socket(multicast_group=multicast_group)

        game_listener = GameListener(multicast_socket=self._multicast_socket)
        game_sender = GameSender(multicast_socket=self._multicast_socket)

        self._view = View()
        self._model = Model(1, 2)

        self._controller = Controller(view=self._view, model=self._model, game_listener=game_listener,
                                       game_sender=game_sender, game_config=self._game_config)
    
    def _load_config(self):
        with open('config.yaml', 'r') as f:
            return yaml.safe_load(f) 

    def _create_multicast_socket(self, multicast_group):
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        udp_socket.bind(('', 9192))
        
        mreq = struct.pack("4s4s", socket.inet_aton(multicast_group[0]), socket.inet_aton('0.0.0.0'))

        udp_socket.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
        udp_socket.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)
        
        return udp_socket
    
