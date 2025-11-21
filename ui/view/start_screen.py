from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QLineEdit, QVBoxLayout, QLabel, QTextEdit
from PyQt6.QtCore import Qt 
class StartScreen(QMainWindow):
    def __init__(self, app_title: str, view_width: int, view_height: int) -> None:
        super().__init__()
        self.setWindowTitle(app_title)  
        self.setFixedSize(view_width, view_height)

        _central_widget = QWidget()
        self.setCentralWidget(_central_widget)
        
        _layout = QVBoxLayout()
        _layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        title = QLabel('Snake')
        title.setStyleSheet("font-size: 150px; font-weight: bold;")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        _layout.addWidget(title)
        
        self._game_list = QLabel()
        self._game_list.setText('списочек\n 2списочек')
        self._game_list.setAlignment(Qt.AlignmentFlag.AlignCenter)
        _layout.addWidget(self._game_list)
        
        

        self._start_game_button = QPushButton()
        self._start_game_button.setText('New game')
        _layout.addWidget(self._start_game_button)
        
        
        

       
        
        _central_widget.setLayout(_layout)

        self.show()