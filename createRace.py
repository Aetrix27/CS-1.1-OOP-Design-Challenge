from cyborg import Cyborg
from animal import Animal
from item import Item

import random

gameRunning = True
itemNames = ["item1", "item2", "item3"]
enemyItemNames = ["enemyItem1", "enemyItem2", "enemyItem3"]

while gameRunning == True:
    #powerUp1 = PowerUp("Speed", 100)
    playerGetItemChance = random.randint(0,2)
    playerGotItem = False
    enemyGetItemChance = random.randint(0,2)
    enemyGotItem = False

    enemyRacer = Cyborg(False)
    species = input("Do you want to be a cyborg (110 Health and 30 speed), animal (100 Health and 35 speed), or cyborgAnimal (105 Health and 32.5 speed?")
    if species == "cyborg":
        playerRacer = Cyborg(True)
    elif species == "animal":
        playerRacer = Animal()

    for possibleItem in range(3):
        #if playerGetItemChance == 1:
        itemNames[possibleItem] = Item()
        itemNames[possibleItem].randomItem()
        playerRacer.addItem(itemNames[possibleItem])
        playerRacer.totalBoost()
        print(playerRacer.speed)

        enemyItemNames[possibleItem] = Item()
        enemyItemNames[possibleItem].randomItem()
        enemyRacer.addItem(enemyItemNames[possibleItem])
        enemyRacer.totalBoost()
        print(enemyRacer.speed)

    gameRunning = False

    #if item1.selectedItem == 0

    #print(playerRacer.totalPowerUp())
    #powerup1 = PowerUp("Booma")
    #playerRacer.getPowerUp(powerup1)
    #print(playerRacer.totalPowerUp())
