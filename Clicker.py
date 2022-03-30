from abc import ABC, abstractmethod

class Clicker(ABC):
    """Abstract class Clicker"""
    def __init__(self, stopbutton: str):
        self.stopbutton: str = stopbutton

    @abstractmethod
    def start(self) -> None:
        pass