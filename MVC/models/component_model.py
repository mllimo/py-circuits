import pyray as pr



class ComponentModel:
    def __init__(self) -> None:
        self._position = pr.Vector2()


    def get_position(self) -> pr.Vector2:
        return pr.Vector2(self._position.x, self._position.y)


    def set_position(self, pos: pr.Vector2):
        self._position.x = pos.x
        self._position.y = pos.y
        self._set_position(pos)


    def _set_position(self, pos: pr.Vector2):
        pass
