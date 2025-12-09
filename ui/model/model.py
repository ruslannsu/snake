from ui.model.cell_types import CellType

class Model:
    def __init__(self, width, height) -> None:
        self._field_matrix = []
        for i in range(height):
            self._field_matrix.append([])

        for i in range(height):
            for _ in range(width):
                self._field_matrix[i].append(CellType.EMPTY)

    def update_model(self):
        pass
    

    