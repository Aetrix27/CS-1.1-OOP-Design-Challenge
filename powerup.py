from item import Item
import random

class PowerUp(Item):
    def increaseSpeed(self):
        random_speed = random.randint(0, 10)
        return random_speed

    #def takeChance():
      #  print("fdsa")
      

