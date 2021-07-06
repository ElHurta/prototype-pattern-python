from abc import ABC, abstractmethod

# Class Creation
class Prototype(ABC):

    # Constructor:
    def __init__(self):
        # Base attributes
        self.height = None
        self.age = None
        self.defense = None
        self.attack = None

    # Clone Method:
    @abstractmethod
    def clone(self):
        pass  