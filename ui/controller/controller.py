from ui.model.model import Model
from ui.view.view import View

class Controller:
    def __init__(self, view: View, model: Model) -> None:
        self._view = view
        self._model = model
        


