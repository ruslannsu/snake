from ui.model.model import Model
from ui.view.view import View

from snake.game.listener import GameListener
from snake.game.sender import GameSender
from event_bus.event_bus import event_bus
from snake.game.game_config import GameConfig
from snake.game.roles import Roles
from proto.proto_messages import ProtoMessages

class Controller:
    def __init__(self, view: View, model: Model, game_listener: GameListener, game_sender: GameSender, game_config: GameConfig) -> None:
        self._view = view
        self._model = model
        self._game_role = None
        self._game_listener = game_listener
        game_listener.start()
        self._game_config = game_config

        self._proto_messages = ProtoMessages()

        self._game_sender = game_sender
        
        event_bus.subscribe(event_name="start_game", handler=self._set_master_role)
        event_bus.subscribe(event_name='get_announcement', handler=self._update_game_list)


    def _update_game_list(self):
        if self._game_role == None:
            messages = self._game_listener.messages
            game_list = ''

            for msg in messages:
                game_name = self._proto_messages.get_game_name(msg)
                game_list += str(game_name)
            

            self._view._start_screen._set_game_list(game_list)
            
        
    def _set_master_role(self):
        
        self._game_role = Roles.MASTER

        self._game_sender._message = self._proto_messages.create_announcement_message(game_name='random', can_join=True, 
                                                                                       width=self._game_config.field_width,
                                                                                       height=self._game_config.field_height,
                                                                                       food_static=self._game_config.food_static,
                                                                                        delay=self._game_config.delay, player_score=0, 
                              
                                                                                       player_role=Roles.MASTER, player_id=123, player_name='user1') 
        self._game_sender.start()
    
    def _set_default_role(self):
        self._game_role = Roles.DEFAULT
        

