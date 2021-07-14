from prototype import Prototype
import copy

class Shopkeeper(Prototype):
    def __init__(self):
        super().__init__()

        # New Values for the Base Attributes:
        self.height = 1.64
        self.age = 22
        self.defense = 32
        self.attack = 16

        # Particular Attribute
        self.charisma = 30

    # Overwritting Cloning Method:
    def clone(self):
        # Copy function provided by Python
        return copy.copy(self)    
    
