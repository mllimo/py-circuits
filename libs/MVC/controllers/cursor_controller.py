from typing import Tuple

import pyray as pr

from libs.MVC.controllers.component_controller import ComponentController
from libs.MVC.models.cursor_model import CursorModel
from libs.utils.singleton import SingletonMeta

class CursorController(ComponentController, metaclass=SingletonMeta):
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