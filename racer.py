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
        #Adds the most current item
        if (self.items[-1] == "Jet Booster" or self.items[-1] == "Speed Booster"):
            boost_total += self.items[-1].increaseSpeed()
        self.speed += boost_total
        return boost_total
    
    def totalPowerUp(self):
        boost_total = 0
        boost_total += self.boosts[-1].increaseSpeed()
        self.speed += boost_total
        return boost_total

    def returnSpeed(self):
      return f"The speed of {self.name} is now {self.speed}"


