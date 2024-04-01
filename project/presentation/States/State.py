from __future__ import annotations
from abc import ABC, abstractmethod

class State(ABC):
    app = None

    def __init__(self, application):
        self.app = application

    @staticmethod
    def get_state(application):
        return State(application)

    @abstractmethod
    def buildInterface(self) -> None:
        pass

    @abstractmethod
    def destroyInterface(self) -> None:
        pass