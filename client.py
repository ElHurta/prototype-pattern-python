from shopkeeper import Shopkeeper
from warrior import Warrior
from mage import Mage

import datetime

def npc_creation():
    
    while(True):

        # Variable that we'll use to store the choosen NPC:
        id = int(input('Enter the number of the NPC you want to create: 1. Shopkeeper, 2. Warrior, 3. Mage: '))
        
        print('Starting NPC Creation at ', datetime.datetime.now().time())
        if id == 1:
            return Shopkeeper()
        elif id == 2:
            return Warrior()
        elif id == 3:
            return Mage()
        else:
            print("The option introduced is not valid, please check your input and try again")    

if __name__ == '__main__':
    
    newNPC = npc_creation()
    print('NPC Creation Successful |', 'NPC Created: ' + newNPC.__class__.__name__ + ' At', datetime.datetime.now().time())
    print('Attributes: ' + ', '.join("%s: %s" % item for item in vars(newNPC).items()))
    print('---------------------------------------')

    clonedNPC = newNPC.clone()
    print('NPC Cloning Successful |',  'NPC Cloned: ' + clonedNPC.__class__.__name__ + ' At', datetime.datetime.now().time())