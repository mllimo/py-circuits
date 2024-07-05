import pyray as pr

from libs.MVC.models.component_model import ComponentModel
from libs.MVC.controllers.component_controller import ComponentController

class CursorModel(ComponentModel):
    def __init__(self) -> None:
        super().__init__()
        self._selection = None

    def get_selection(self) -> ComponentController:
        return self._selection

    def set_selection(self, selection: ComponentController):
        self._selection = selection