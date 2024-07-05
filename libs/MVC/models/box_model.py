import pyray as pr

from libs.MVC.models.component_model import ComponentModel


class BoxModel(ComponentModel):
    def __init__(self, rectangle: pr.Rectangle) -> None:
        super().__init__()
        self._rectangle = rectangle
        self.set_position(pr.Vector2(rectangle.x, rectangle.y))


    def get_rectangle(self) -> pr.Rectangle:
        return self._rectangle


    def _set_position(self, pos: pr.Vector2):
        self._rectangle.x = pos.x
        self._rectangle.y = pos.y


    def set_size(self, width: int, height: int) -> None:
        self._rectangle.width = width
        self._rectangle.height = height