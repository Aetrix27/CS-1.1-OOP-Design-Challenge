from item import Item
from racer import Racer
import random

class PowerUp(Item):
    def speedUp(self):
        random_int = random.randint(0,60)
        return random_int

    #def takeChance():
      #  print("fdsa")
      

racer1 = Racer(5)