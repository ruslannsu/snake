import arcade
import arcade.gui
class GameScreen(arcade.Window): 
    def __init__(self, width: int, height: int) -> None:
        super().__init__(width=width, height=height)
        
    def _setup_start_screen(self) -> None:
        arcade.set_background_color(color=arcade.color.RED)

    def setup(self):
        self._setup_start_screen()
 
    def on_key_press(self, symbol: int, modifiers: int) -> None:
        print(symbol)

    