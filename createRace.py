from cyborg import Cyborg
from animal import Animal
from powerup import PowerUp
from cyborgAnimal import CyborgAnimal
from item import Item

import random

def checkWinner(firstRacer, secondRacer):
    if firstRacer.speed > secondRacer.speed and firstRacer.health > 0:
        print(f"{firstRacer.name} wins!")
    elif secondRacer.speed > firstRacer.speed and secondRacer.health > 0:
        print(f"{secondRacer.name} wins!")
    elif firstRacer.health > secondRacer.health and firstRacer.health > 0:
        print(f"{firstRacer.name} wins!")
    elif secondRacer.health > firstRacer.health and secondRacer.health > 0:
        print(f"{secondRacer.name} wins!")
    else:
        print("It's a tie!")

class createRace():
    def race(self):
        gameRunning = True
        itemNames = ["item1", "item2", "item3"]
        enemyItemNames = ["enemyItem1", "enemyItem2", "enemyItem3"]

        while gameRunning == True:
            randEnemyClasses = [Cyborg(False, "Cybertron"), Animal(False, "Nike"), CyborgAnimal(False, "Hybrid")]   
            enemyRacer = random.choice(randEnemyClasses)
            species = input("Do you want to be a cyborg (110 Health and 30 speed), animal (100 Health and 35 speed), or cyborgAnimal (105 Health and 32.5 speed)?\n")
            name = input("What will your name be?\n")

            if species == "cyborg":
                playerRacer = Cyborg(True, name)
            elif species == "animal":
                playerRacer = Animal(True, name)
            elif species == "cyborgAnimal":
                playerRacer = CyborgAnimal(True, name)

            for possibleItem in range(3):
                playerGetItemChance = random.randint(0,5)
                playerGetPowerUpChance = random.randint(0,2)
                playerGotPowerUp = False
                playerGotItem = False
                enemyGetItemChance = random.randint(0,2)
                enemyGetPowerUpChance = random.randint(0,5)
                enemyGotPowerUp = False
                enemyGotItem = False

                if playerGetItemChance == 0:
                    playerGotItem = True
                                
                if enemyGetItemChance == 0:
                    enemyGotItem = True

                if playerGetPowerUpChance == 1:
                    playerGotItem = True
                
                if enemyGetPowerUpChance == 1:
                    playerGotItem = True

                if playerGotItem == True:
                    itemNames[possibleItem] = Item()
                    itemNames[possibleItem].randomItem(playerRacer)
                    playerRacer.addItem(itemNames[possibleItem])
                    playerRacer.totalBoost()
                    print(playerRacer.returnSpeed())

                if enemyGotItem == True:
                    enemyItemNames[possibleItem] = Item()
                    enemyItemNames[possibleItem].randomItem(enemyRacer)
                    enemyRacer.addItem(enemyItemNames[possibleItem])
                    enemyRacer.totalBoost()
                    print(enemyRacer.returnSpeed())

                if playerGotPowerUp == True:
                    powerup1 = PowerUp()
                    playerRacer.getPowerUp(powerup1)
                    playerRacer.totalPowerUp()
                    playerRacer.returnSpeed()
                    print(playerRacer.returnSpeed())

                if enemyGotPowerUp == True:
                    powerup2 = PowerUp()
                    enemyRacer.getPowerUp(powerup2)
                    enemyRacer.totalPowerUp()
                    enemyRacer.returnSpeed()
                    print(enemyRacer.returnSpeed())
                
            checkWinner(playerRacer, enemyRacer)

            gameRunning = False

newRace = createRace()
newRace.race()