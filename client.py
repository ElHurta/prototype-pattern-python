from npc1 import NPC1
from npc2 import NPC2
from npc3 import NPC3


def npc_creation():

    while(True):

        # Variable that we'll use to store the choosen NPC:
        id = int(input('Enter the number of the NPC you want to create: 1. NPC1, 2. NPC2, 3. NPC3: '))
        
        if id == 1:
            return NPC1()
        elif id == 2:
            return NPC2()
        elif id == 3:
            return NPC3()
        else:
            print("The option introduced is not valid, please check your input and try again")    

if __name__ == '__main__':
    
    newNPC = npc_creation()

    print('NPC Creation Successful: \n' + 'NPC Created: ' + newNPC.__class__.__name__)
    print('Attributes: ' + ', '.join("%s: %s" % item for item in vars(newNPC).items()))