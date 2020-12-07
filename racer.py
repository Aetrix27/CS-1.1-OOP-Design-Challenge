from powerup import PowerUp
from item import Item
import random

class Racer:
    def __init__(self, health, speed):
        self.speed = speed
        self.health = health
        self.boosts = list()
        self.items = list()

    def speak(self, message):
        print(message)

    def getPowerUp(self, powerUp):
        self.boosts.append(powerUp)

    def addItem(self, item):
        self.items.append(item)
    
    def totalBoost(self):
        boost_total = 0
        for item in self.items:
            boost_total += item.increaseSpeed()
        self.speed += boost_total
        return boost_total
    
    def totalPowerUp(self):
        boost_total = 0
        for boost in self.boosts:
            boost_total += boost.increaseSpeed()
        self.speed += boost_total
        return boost_total

    def isAlive(self):
        if self.health > 0:
            return True
        elif self.health <= 0:
            return False

    def hitOtherPlayer(self, enemy):
        for item in self.items:
            if item.selectedItem == 1:
                if self.isAlive() and enemy.isAlive():
                    enemy.health -= item.attack()

    def checkWinner(self, racer1, racer2):
        if racer1.speed > 100 and racer1.speed > racer2.speed:
            print("Racer1 wins!")
        elif racer2.speed > 100 and racer2.speed > racer1.speed:
            print("Racer 2 wins!")
        elif racer1.speed == racer2.speed:
            print("It's a tie!")
            #gameRunning=false

