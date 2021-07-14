from abc import ABC, abstractmethod
import time

# Class Creation
class Prototype(ABC):

    # Constructor:
    def __init__(self):
        # Base attributes
        self.height = None
        self.age = None
        self.defense = None
        self.attack = None

        # Delay for example purposes
        time.sleep(3)
        

    # Clone Method:
    @abstractmethod
    def clone(self):
        pass  