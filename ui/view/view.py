from ui.view.game_screen import GameScreen
from ui.view.start_screen import StartScreen


class View: 
    def __init__(self) -> None:
        self._start_screen = StartScreen('Snake', 300, 300)
        self._game_screen = GameScreen(100, 100)
        

        



