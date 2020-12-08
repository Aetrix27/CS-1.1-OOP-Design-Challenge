from powerup import PowerUp
from item import Item
import random

class Racer:
    def __init__(self, health, speed, name):
        self.speed = speed
        self.name = name
        self.health = health
        self.boosts = list()
        self.items = list()

    def getPowerUp(self, powerUp):
        #This function adds a powerup to the list
        self.boosts.append(powerUp)

    def addItem(self, item):
        #This function adds an item to the list
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

    def returnSpeed(self):
      return f"The speed of {self.name} is now {self.speed}"


