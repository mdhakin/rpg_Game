from Map import *
import random
from Player import *
from Monster import *


def main():
    
    mainPlayer = Player()
    gameMap = Map()
    
    done = False
    
    while not done:
        gameMap.printPlayerPos()
        
        selection = 1
        
        print("1) Move, 2) Rest, 3) View Stats, 4) Quit: ")
        selection = int(input())
        monster = 0
        
        if selection == 1:
            gameMap.movePlayer()
            
            # Check for random encounter. This function
            # returns a null pointer if no monsters are
            # encountered.
            
            monster = gameMap.checkRandomEncounter()
            
            # 'monster' not numm, run combat simulation
            if monster != 0:
                while True:
                    mainPlayer.displayHitPoints()
                    monster.displayHitPoints()
                    
                    runAway = mainPlayer.attack(monster)
                    
                    if runAway:
                        break
                    
                    if monster.isDead():
                        mainPlayer.victory(monster.getXPReward())
                        mainPlayer.levelUp()
                        break
                        
                    
                    monster.attack(mainPlayer)
                    
                    if mainPlayer.isDead():
                        mainPlayer.gameover()
                        done = True
                        break
                        
            monster = 0
            
                    
        elif selection == 2:
            mainPlayer.rest()
        elif selection == 3:
            mainPlayer.viewStats()
        else:
            print("Thank you for playing.")
            done = True
            
        
    
main()