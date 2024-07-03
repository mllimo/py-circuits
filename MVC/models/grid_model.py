import pyray as pr

from MVC.models.component_model import ComponentModel
from MVC.controllers.component_controller import ComponentController

import utils
import utils.list

class GridModel(ComponentModel):

    class Cell:
        def __init__(self) -> None:
            self.width = 0
            self.height = 0
            self.content = None


    def __init__(self) -> None:
        super().__init__()
        self._rows = 0
        self._columns = 0
        self._size = pr.Vector2()
        self._cells = []
        self._color = pr.GREEN


    def set_color(self, color: pr.Color):
        self._color = color


    def set_rows_columns(self, size: pr.Vector2):
        self._columns = int(size.x)
        self._rows = int(size.y)
        self._cells = utils.list.resize_list(self._cells, self._columns * self._rows, default_value=GridModel.Cell())
        self._readjust_cells_size(self._size)


    def set_size(self, size: pr.Vector2):
        self._size = size
        self._readjust_cells_size(size)


    def at(self, x, y) -> Cell:
        index = self._2d_to_1d(pr.Vector2(x, y))
        if index >= len(self._cells):
            raise IndexError("Índice fuera de rango")

        return self._cells[index]


    def get_rows_columns(self) -> pr.Vector2:
        return pr.Vector2(self._columns, self._rows)


    def get_color(self) -> pr.Color:
        return self._color


    def _readjust_cells_size(self, size: pr.Vector2):
        if self._columns == 0 or self._rows == 0:
            return

        x_size = size.x / self._columns
        y_size = size.y / self._rows

        for i in range(self._rows):
            for j in range(self._columns):
                cell = self.at(j, i)
                cell.width = int(x_size)
                cell.height = int(y_size)


    def _2d_to_1d(self, pos: pr.Vector2) -> int:
        return int(pos.y) * self._columns + int(pos.x)


    def _1d_to_2d(self, index: int) -> pr.Vector2:
        row = index // self._columns
        column = index % self._columns
        return pr.Vector2(column, row)