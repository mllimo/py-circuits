import enum


class Event:

    class Kind(enum.Enum):
        UNDEFINED = 0
        MOUSE = 1
        KEYBOARD = 2

    class Type(enum.Enum):
        UNDEFINED = 0
        DOWN = 1
        UP = 2
        PRESSED = 3
        RELEASED = 4


    def __init__(self) -> None:
        self._kind = Event.Kind.UNDEFINED
        self._type = Event.Type.UNDEFINED
        self._button = None


    def type(self) -> Type:
        return self._type


    def kind(self) -> Kind:
        return self._kind


    def button(self):
        return self._button


    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Event):
            return False
        
        return self.button() == value.button() \
                and self.kind() == value.kind() \
                and self.type() == value.type()