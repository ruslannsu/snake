from view.game_screen import GameScreen
from view.start_screen import StartScreen


class View: 
    def __init__(self, game_screen: GameScreen, start_screen: StartScreen) -> None:
        self._start_screen = start_screen
        self._game_screen = game_screen
        
        
        



