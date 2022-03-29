class ManualClass:
    def __init__(self, id: int, text: str):
        self._id: int = id
        self._text: str = text

    @property
    def id(self):
        return self._id
    @property
    def text(self):
        return self._text

    def __repr__(self):
        return f'{self.__class__.__name__}, {self._id}, {self._text}'

    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return other.id == self._id and self._text == other.text
        else:
            return NotImplemented

    def __nq__(self, other):
        result = self.__eq__(other)

        if result is NotImplemented:
            return NotImplemented
        else:
            return not result

    def __hash__(self):
        return hash((self.__class__, self._id, self._text))
