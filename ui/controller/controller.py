from ui.model.model import Model
from ui.view.view import View
from snake.roles.master import Master
from snake.game.listener import GameListener
from snake.game.sender import GameSender
from event_bus.event_bus import event_bus

class Controller:
    def __init__(self, view: View, model: Model, master_role: Master, game_listener: GameListener, game_sender: GameSender) -> None:
        self._view = view
        self._model = model
        self._master_role = master_role
        self._game_role = None
        self._game_listener = game_listener
        game_listener.start()

        self._game_sender = game_sender
        self._game_sender.start()

        event_bus.subscribe(event_name="start_game", handler=self._set_master_role)
        
    def _set_master_role(self):
        self._game_role = self._master_role
        self._game_role._send_game_anouncment()
        print('sended')


