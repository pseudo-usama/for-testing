from abc import ABCMeta, abstractmethod


class MyAbstractClass(metaclass=ABCMeta):
    def __init__(self):
        pass

    @property
    @abstractmethod
    def path(self):
        pass
