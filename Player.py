import random
from time import time
from Range import *
from Weapon import *
from Monster import *

class Player:
    mName = ""
    mClassName = ""
    mAccuracy = 0
    mHitPoints = 0
    mMaxHitPoints = 0
    mExpPoints    = 0
    mNextLevelExp = 0
    mLevel        = 0
    mArmor        = 0
    mWeapon = Weapon(Range(0,0),"")
    
    def __init__(self):
        
        print("CHARACTER CLASS GENERATION")
        print("==========================")
        
        # Input character's name.
        nInput = str(input("Enter your character's name: "))
        
        self.mName = nInput
        
        # Character selection.
        print("Please select a character class number...")
        print("1)Fighter 2)Wizard 3)Cleric 4)Thief : ")
        
        characterNum = 1
        characterNum = int(input())
        
        if(characterNum == 1):
            self.mClassName = "Fighter"
            self.mAccuracy     = 10
            self.mHitPoints    = 20
            self.mMaxHitPoints = 20
            self.mExpPoints    = 0
            self.mNextLevelExp = 1000
            self.mLevel        = 1
            self.mArmor        = 4
            self.mWeapon.mName = "Long Sword"
            self.mWeapon.mDamageRange.mLow  = 1
            self.mWeapon.mDamageRange.mHigh = 8
        elif (characterNum == 2):
            self.mClassName = "Wizard"
            self.mAccuracy     = 5
            self.mHitPoints    = 10
            self.mMaxHitPoints = 10
            self.mExpPoints    = 0
            self.mNextLevelExp = 1000
            self.mLevel        = 1
            self.mArmor        = 1
            self.mWeapon.mName = "Staff"
            self.mWeapon.mDamageRange.mLow  = 1
            self.mWeapon.mDamageRange.mHigh = 4
        elif (characterNum == 3):
            self.mClassName = "Cleric"
            self.mAccuracy     = 8
            self.mHitPoints    = 15
            self.mMaxHitPoints = 15
            self.mExpPoints    = 0
            self.mNextLevelExp = 1000
            self.mLevel        = 1
            self.mArmor        = 3
            self.mWeapon.mName = "Flail"
            self.mWeapon.mDamageRange.mLow  = 1
            self.mWeapon.mDamageRange.mHigh = 6
        else:
            self.mClassName = "Thief"
            self.mAccuracy     = 7
            self.mHitPoints    = 12
            self.mMaxHitPoints = 12
            self.mExpPoints    = 0
            self.mNextLevelExp = 1000
            self.mLevel        = 1
            self.mArmor        = 2
            self.mWeapon.mName = "Short Sword"
            self.mWeapon.mDamageRange.mLow  = 1
            self.mWeapon.mDamageRange.mHigh = 6
            
    def attack(self, mMonster):
        # Combat is turned based: display an options menu.  You can,
	    # of course, extend this to let the player use an item,
	    # cast a spell, and so on.
        
        selection = 1
        print("1) Attack, 2) Run: ")
        selection = int(input())
        
        if selection == 1:
            print("You attack an " + mMonster.mName + " with a " + self.mWeapon.mName)
            random.seed(time())
            if (random.randint(0, 20) < self.mAccuracy):
                damage = random.randint(self.mWeapon.mDamageRange.mLow, self.mWeapon.mDamageRange.mHigh)
                totalDamage = damage - mMonster.getArmor()
                
                if totalDamage <= 0:
                    print("Your attack failed to penetrate the armor.")
                else:
                    print("Your attack for " + str(totalDamage) + " damage!")
                    mMonster.takeDamage(totalDamage)
                    
            else:
                print("You Miss!")
                
                
        elif selection == 2:
            random.seed(time())
            roll = random.randint(1, 4)
            if roll == 1:
                print("You run away!")
                return True
            else:
                print("You could not escape!")
                
        return False
        
        
        
        
    def levelUp(self):
        if self.mExpPoints >= self.mNextLevelExp:
            print("You gained a level!")

		    # Increment level.
            self.mLevel = self.mLevel + 1

		    # Set experience points required for next level.
            self.mNextLevelExp = self.mLevel * self.mLevel * 1000;

            # Increase stats randomly.
            self.mAccuracy     += random.randint(1, 3)
            self.mMaxHitPoints += random.randint(2, 6);
            self.mArmor        += random.randint(1, 2);

            # Give player full hitpoints when they level up.
            self.mLevel = self.mMaxHitPoints;
            return
	
    
    def rest(self):
        print("Resting...")

        self.mHitPoints = self.mMaxHitPoints;

        # TODO: Modify function so that random enemy encounters
        # are possible when resting.
    
    def viewStats(self):
        print("PLAYER STATS")
        print("============")
        

        print("Name            = " + self.mName)
        print("Class           = " + self.mClassName)
        print("Accuracy        = " + str(self.mAccuracy))
        print("Hitpoints       = " + str(self.mHitPoints))
        print("MaxHitpoints    = " + str(self.mMaxHitPoints))
        print("XP              = " + str(self.mExpPoints))
        print("XP for Next Lvl = " + str(self.mNextLevelExp))
        print("Level           = " + str(self.mLevel))
        print("Armor           = " + str(self.mArmor))
        print("Weapon Name     = " + str(self.mWeapon.mName))
        print("Weapon Damage   = " + str(self.mWeapon.mDamageRange.mLow) + "-" + str(self.mWeapon.mDamageRange.mHigh))

        print("END PLAYER STATS")
        print("================")
    
    def victory(self,xp):
        print("You won the battle!")
        print("You win " + str(xp) + " experience points!")

        self.mExpPoints += xp;
    
    
    
    def gameover(self):
        print("You died in battle...")
        print("================================")
        print("GAME OVER!")
        print("================================")
        print("Press 'q' to quit: ")
        q = 'q'
        q = str(input())

    
    def displayHitPoints(self):
        print(self.mName + "'s hitpoints = " + str(self.mHitPoints))
        
    def getArmor(self):
        return self.mArmor
    
    def takeDamage(self, damage):
        self.mHitPoints = self.mHitPoints - damage
    
    def isDead(self):
        return self.mHitPoints <= 0
    