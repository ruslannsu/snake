import arcade
from ui.view.start_screen import StartScreen
from PyQt6.QtWidgets import QApplication
from snake.game.game import Game

def main():
    app = QApplication([])
    game = Game()
    
    
    app.exec()
    
    arcade.run()

if __name__ == "__main__":
    main() 
