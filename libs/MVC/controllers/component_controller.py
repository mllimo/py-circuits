import pyray as pr

from libs.MVC.models.component_model import ComponentModel
from libs.MVC.views.component_view import ComponentView


class ComponentController:
    def __init__(self, model: ComponentModel, view: ComponentView) -> None:
        self._model = model
        self._view = view

    def get_position(self) -> pr.Vector2:
        return self._model.get_position()


    def set_position(self, pos: pr.Vector2):
        self._model.set_position(pos)


    def display(self):
        self._view.display(self._model)