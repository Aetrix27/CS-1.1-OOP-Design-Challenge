import random

class Item:
    def __init__(self):
        self.max_speed = 5
        self.itemArr = ["Jet Booster", "Speed Booster", "A Mine", "Brick Wall"]
    
    def increaseSpeed(self):
        random_speed = random.randint(0, int(self.max_speed))
        return random_speed

    def randomItem(self, racer):
        random_item = random.choice(self.itemArr)
        if(random_item == "A Mine" or random_item == "Brick Wall"):
            print("You take damage!")
            racer.health -= 50
        print(f"You picked up {random_item}!")





