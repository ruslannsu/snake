

class GameConfig:
    def __init__(self, field_width, field_height, delay, food_static, grid_size, sidebar_width) -> None:
        self._field_width = field_width
        self._field_height = field_height
        self._delay = delay
        self._food_static = food_static
        self._grid_size = grid_size
        self._sidebar_width = sidebar_width

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
    
    @property
    def sidebar_width(self):
        return self._sidebar_width
    
    @property
    def grid_size(self):
        return self._grid_size