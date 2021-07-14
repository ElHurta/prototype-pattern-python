from prototype import Prototype
import copy

class Mage(Prototype):
    def __init__(self):
        super().__init__()

        # New Values for the Base Attributes:
        self.height = 1.80
        self.age = 37
        self.defense = 25
        self.attack = 32

        # Particular Attribute
        self.mana = 100

    # Overwritting Cloning Method
    def clone(self):
        # Copy function provided by Python
        return copy.copy(self)  