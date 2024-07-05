import pyray as pr

from events.event import Event

class MouseEvent(Event):

    MOUSE_BUTTONS = [
        pr.MouseButton.MOUSE_BUTTON_LEFT ,
        pr.MouseButton.MOUSE_BUTTON_RIGHT ,
        pr.MouseButton.MOUSE_BUTTON_MIDDLE
    ]


    def __init__(self, button: pr.MouseButton, _type = Event.Type.UNDEFINED) -> None:
        super().__init__()
        self._kind = Event.Kind.MOUSE
        self._type = _type
        self._button = button
        self.begin_pos = (pr.get_mouse_position().x, pr.get_mouse_position().y)
        self.end_pos = (0, 0)


    def __eq__(self, value: object) -> bool:
        if not super().__eq__(value) or not isinstance(value, MouseEvent):
            return False
        return True