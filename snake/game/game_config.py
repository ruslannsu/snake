

class GameConfig:
    def __init__(self, field_width, field_height, delay, food_static) -> None:
        self._field_width = field_width
        self._field_height = field_height
        self._delay = delay
        self._food_static = food_static

    @property
    def field_width(self):
        return self._field_width
    
    @property
    def field_height(self):
        return self._field_height
    
    @property
    def delay(self):
        return self._delay
    
    @property
    def food_static(self):
        return self._food_static