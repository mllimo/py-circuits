from typing import Tuple

import pyray as pr

from libs.MVC.controllers.component_controller import ComponentController
from libs.MVC.models.box_model import BoxModel
from libs.MVC.views.box_view import BoxView

class BoxController(ComponentController):
    def __init__(self, rectangle: pr.Rectangle) -> None:
        super().__init__(BoxModel(rectangle), BoxView())


    def get_position(self) -> pr.Vector2:
        return pr.Vector2(self._model.get_rectangle().x, self._model.get_rectangle().y)


    def get_rect(self):
        return self._model.get_rectangle()


    def set_position(self, pos: pr.Vector2):
        self._model.set_position(pos)


    def set_color(self, color: pr.Color):
        self._view.color = color


    def set_texture(self, texture: pr.Texture2D):
        self._view.texture = texture


    def display(self):
        self._view.display(self._model)