from prototype import Prototype
import copy

class NPC2(Prototype):
    def __init__(self):
        super().__init__()

        # New Values for the Base Attributes:
        self.height = 1.71
        self.age = 42
        self.defense = 13
        self.attack = 18

    # Overwritting Cloning Method
    def clone(self):
        # Copy function provided by Python
        return copy.copy(self)  