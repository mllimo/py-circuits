from typing import Tuple

import pyray as pr

from MVC.controllers.component_controller import ComponentController
from MVC.models.cursor_model import CursorModel

class CursorController(ComponentController):
    def __init__(self) -> None:
        super().__init__(CursorModel(), None)

    def get_selection(self) -> ComponentController:
        model: CursorModel = self._model
        return model.get_selection()


    def set_selection(self, selection: ComponentController):
        model: CursorModel = self._model
        model.set_selection(selection)


    def display(self):
        pass
        #self._view.display(self._model)