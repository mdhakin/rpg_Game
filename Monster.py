import random
from Range import *
from Weapon import *
from Player import *


class Monster:
    mName = ""
    mHitPoints = 0
    mAccuracy = 0
    mExpReward = 0
    mArmor = 0
    mWeapon = Weapon(Range(0,0),"")
    
    def __init__(self, name, hp, acc, xpRew, armor, weaponName, lowDamage, highDamage):
        self.mName = name
        self.mHitPoints = hp
        self.mAccuracy = acc
        self.mExpReward = xpRew
        self.mArmor = armor
        self.mWeapon.mDamageRange.mHigh = highDamage
        self.mWeapon.mDamageRange.mLow = lowDamage
        self.mWeapon.mName = weaponName
    
    def getArmor(self):
        return self.mArmor
    
    def isDead(self):
        return self.mHitPoints <= 0
    
    def getXPReward(self):
        return self.mExpReward
    
    def attack(self, playerList):
        print("A " + self.mName + " attacks you with a " + self.mWeapon.mName)
        tempPlayer = playerList
        # Test to see if the monster hit the player
        random.seed(time())
        if random.randint(0,20) < self.mAccuracy:
            damage = random.randint(self.mWeapon.mDamageRange.mLow, self.mWeapon.mDamageRange.mHigh)
            
            # Subtract player's armor from damage to
            # simulate armor weakening the attack. Note that
            # if the armor > damage this results in a negative 
            # number
            totalDamage = damage - tempPlayer.getArmor()
            
            # If totalDamage <= 0, then we say that, although
            # the attack hit, it did not penetrate the armor
            if totalDamage <= 0:
                print("The monsters attack failed to penetrate your armor.")
            else:
                print("You are hit for " + str(totalDamage) + " damage")
                
                # Subtract from players hitpoints.
                tempPlayer.takeDamage(totalDamage)
            
        else:
            print("The " + self.mName + " missed!")
    
    def takeDamage(self, damage):
        self.mHitPoints = self.mHitPoints - damage
    
    def displayHitPoints(self):
        print(self.mName + "'s jit points = " + str(self.mHitPoints))
    
    def getName(self):
        return self.getName