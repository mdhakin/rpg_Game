import random
from Monster import *

class Map:
    mPlayerXPos = 0
    mPlayerYPos = 0
    
    def getPlayerXPos(self):
        return self.mPlayerXPos
    
    def getPlayerYPos(self):
        return self.mPlayerYPos
    
    def movePlayer(self):
        selection = 1
        
        print("1) North, 2) East, 3) South, 4) West: ")
        
        selection = int(input())
        
        if selection == 1:
            self.mPlayerYPos = self.mPlayerYPos + 1
            
            
        elif selection == 2:
            self.mPlayerXPos = self.mPlayerXPos + 1
            
            
        elif selection == 3:
            self.mPlayerYPos = self.mPlayerYPos - 1
            
            
        elif selection == 4:
            self.mPlayerXPos = self.mPlayerXPos - 1
            
            
        
        
        
        
    def printPlayerPos(self):
        print("Player Position = (" + str(self.mPlayerXPos) + ", " + str(self.mPlayerYPos) + ")")
        
    
    def checkRandomEncounter(self):
        random.seed(time())
        roll = random.randint(0,20)
        
        monster = 0
        
        if roll <= 5:
            return 0
            
        elif roll >= 6 and roll <= 10:
            monster = Monster("Orc", 10, 8, 200, 1, "Short Sword", 2, 7)
            
            print("You encountered an Orc!")
            print("Prepare for battle!")
            
        elif roll >= 11 and roll <= 15:
            monster = Monster("Goblin", 6, 6, 100, 0, "Dagger", 1, 5)
            
            print("You encountered an Goblin!")
            print("Prepare for battle!")
            
        elif roll >= 16 and roll <= 19:
            monster = Monster("Ogre", 20, 12, 500, 2, "Club", 3, 8)
            
            print("You encountered an Ogre!")
            print("Prepare for battle!")
        elif roll == 20:
            print("Orc Lord", 25, 15, 2000, 5, "Two Handed Sword", 5, 20)
            
            print("You encountered an Ogre!")
            print("Prepare for battle!")
        
        return monster
        