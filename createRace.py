from cyborg import Cyborg
from animal import Animal
from powerup import PowerUp
from item import Item

import random

def checkWinner(firstRacer, secondRacer):
    if firstRacer.speed > secondRacer.speed:
        print(f"{firstRacer.name} wins!")
    elif secondRacer.speed > firstRacer.speed:
        print(f"{secondRacer.name} wins!")
    elif firstRacer.speed == secondRacer.speed:
        print("It's a tie!")
        
gameRunning = True
itemNames = ["item1", "item2", "item3"]
enemyItemNames = ["enemyItem1", "enemyItem2", "enemyItem3"]

while gameRunning == True:   
    enemyRacer = Cyborg(False, "Cybertron")
    species = input("Do you want to be a cyborg (110 Health and 30 speed), animal (100 Health and 35 speed), or cyborgAnimal (105 Health and 32.5 speed)?\n")
    name = input("What will your name be?\n")

    if species == "cyborg":
        playerRacer = Cyborg(True, name)
    elif species == "animal":
        playerRacer = Animal(True, name)

    for possibleItem in range(3):
        playerGetItemChance = random.randint(0,2)
        playerGotItem = False
        enemyGetItemChance = random.randint(0,2)
        enemyGotItem = False

        itemNames[possibleItem] = Item()
        itemNames[possibleItem].randomItem()
        playerRacer.addItem(itemNames[possibleItem])
        playerRacer.totalBoost()
        print(playerRacer.returnSpeed())

        enemyItemNames[possibleItem] = Item()
        enemyItemNames[possibleItem].randomItem()
        enemyRacer.addItem(enemyItemNames[possibleItem])
        enemyRacer.totalBoost()
        print(enemyRacer.returnSpeed())

        if possibleItem == 2:
            powerup1 = PowerUp()
            playerRacer.getPowerUp(powerup1)
            playerRacer.totalPowerUp()
            playerRacer.returnSpeed()
            print(playerRacer.returnSpeed())

            powerup2 = PowerUp()
            enemyRacer.getPowerUp(powerup2)
            enemyRacer.totalPowerUp()
            enemyRacer.returnSpeed()
            print(enemyRacer.returnSpeed())
        
    checkWinner(playerRacer, enemyRacer)

    gameRunning = False

