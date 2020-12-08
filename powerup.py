from item import Item
import random

class PowerUp(Item):
    def increaseSpeed(self):
        random_speed = random.randint(-5, 20)
        if random_speed < 0:
            print(f"Your speed decreases by {random_speed} since you tripped and couldn't get the power up!")
        elif random_speed > 0:
            print(f"You luckily got a power up! Your speed increases by {random_speed}")
        elif random_speed == 0:
            print(f"The power up was a decoy. Your speed stays the same.")

        return random_speed


