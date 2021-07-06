from prototype import Prototype
import copy

class NPC1(Prototype):
    def __init__(self):
        super().__init__()

        # New Values for the Base Attributes:
        self.height = 1.64
        self.age = 22
        self.defense = 32
        self.attack = 16

        # We are going to call the clone function now to reduce code later:
        self.clone()

    # Overwritting Cloning Method:
    def clone(self):
        # Copy function provided by Python
        return copy.copy(self)    
    
