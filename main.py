import arcade
from ui.view.view import View
from ui.view.start_screen import StartScreen
from PyQt6.QtWidgets import QApplication

def main():
    app = QApplication([])
    v = StartScreen('Snake', 500, 500)
    
    app.exec()
    
    arcade.run()

if __name__ == "__main__":
    main() 
