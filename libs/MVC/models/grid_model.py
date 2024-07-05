import typing

import pyray as pr

from libs.MVC.models.component_model import ComponentModel
from libs.MVC.controllers.component_controller import ComponentController

import libs.utils.list


class GridModel(ComponentModel):

    class Cell:
        def __init__(self, width = 0, height = 0, content = None) -> None:
            self._width = width
            self._height = height
            self._content = content


        def set_content(self, content: ComponentController):
            self._content = content


        def set_width(self, width):
            self._width = width


        def set_height(self, height):
            self._height = height


        def get_width(self) -> int:
            return self._width


        def get_height(self) -> int:
            return self._height


        def get_content(self):
            return self._content


        def copy(self):
            return GridModel.Cell(self._width, self._height, self._content)


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
        self._cells = libs.utils.list.resize_list(self._cells, self._columns * self._rows, default_value=GridModel.Cell())
        self._readjust_cells_size(self._size)


    def set_size(self, size: pr.Vector2):
        self._size = size
        self._readjust_cells_size(size)


    def set_at(self, x, y, element: ComponentController):
        index = self._2d_to_1d(pr.Vector2(x, y))
        if index >= len(self._cells):
            raise IndexError("grid index out of range")

        cell: GridModel.Cell = self._cells[index]
        new_x = self.get_position().x + cell.get_width()   * x
        new_y = self.get_position().y + cell.get_height()  * y
        element.set_position(pr.Vector2(new_x, new_y))
        cell.set_content(element)


    def _set_at(self, x, y, cell: Cell):
        index = self._2d_to_1d(pr.Vector2(x, y))
        if index >= len(self._cells):
            raise IndexError("grid index out of range")

        self._cells[index] = cell


    def get_at(self, x, y) -> Cell:
        index = self._2d_to_1d(pr.Vector2(x, y))
        if index >= len(self._cells):
            raise IndexError("grid index out of range")

        return self._cells[index].copy()


    def get_rows_columns(self) -> pr.Vector2:
        return pr.Vector2(self._columns, self._rows)


    def get_color(self) -> pr.Color:
        return self._color


    def collide_with_index(self, other: pr.Rectangle) -> pr.Vector2:
        current_pos = self.get_position()
        grid_size = self.get_rows_columns()

        for y in range(0, int(grid_size.y)):
            for x in range(0, int(grid_size.x)):
                cell = self.get_at(x, y)
                rect = pr.Rectangle(current_pos.x, current_pos.y, cell.get_width(), cell.get_height())
                if pr.check_collision_recs(rect, other):
                    return pr.Vector2(x, y)
                current_pos.x += cell.get_width()

            current_pos.y += self.get_at(0, y).get_height()
            current_pos.x = self.get_position().x

        return None


    def _readjust_cells_size(self, size: pr.Vector2):
        if self._columns == 0 or self._rows == 0:
            return

        x_size = size.x / self._columns
        y_size = size.y / self._rows

        for y in range(self._rows):
            for x in range(self._columns):
                cell = self.get_at(x, y)
                cell.set_width(int(x_size))
                cell.set_height(int(y_size))
                self._set_at(x, y, cell)


    def _2d_to_1d(self, pos: pr.Vector2) -> int:
        return int(pos.y) * self._columns + int(pos.x)


    def _1d_to_2d(self, index: int) -> pr.Vector2:
        row = index // self._columns
        column = index % self._columns
        return pr.Vector2(column, row)