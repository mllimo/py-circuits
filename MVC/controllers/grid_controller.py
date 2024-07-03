import pyray as pr

from MVC.controllers.component_controller import ComponentController
from MVC.models.grid_model import GridModel
from MVC.views.gird_view import GridView


class GridController(ComponentController):
    def __init__(self) -> None:
        super().__init__(GridModel(), GridView())


    def set_color(self, color: pr.Color):
        model: GridModel = self._model
        model.set_color(color)


    def set_rows_columns(self, size: pr.Vector2):
        model: GridModel = self._model
        model.set_rows_columns(size)


    def set_size(self, size: pr.Vector2):
        model: GridModel = self._model
        model.set_size(size)


    def at(self, x, y) -> GridModel.Cell:
        model: GridModel = self._model
        return model.at(x, y)


    def get_rows_columns(self) -> pr.Vector2:
        model: GridModel = self._model
        return model.get_rows_columns()


    def get_color(self) -> pr.Color:
        model: GridModel = self._model
        return model.get_color()