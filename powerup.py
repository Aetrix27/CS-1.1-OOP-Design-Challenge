from item import Item
import random

class PowerUp(Item):
    def increaseSpeed(self):
        random_speed = random.randint(-20, 20)
        if random_speed < 0:
            print(f"Your speed by {random_speed} decreases since you tripped and couldn't get the power up!")
        elif random_speed > 0:
            print(f"You got the power up! Your speed increases by {random_speed}")
        elif random_speed == 0:
            print(f"The power up was a decoy. Your speed stays the same.")

        return random_speed

    #def takeChance():
      #  print("fdsa")
      

