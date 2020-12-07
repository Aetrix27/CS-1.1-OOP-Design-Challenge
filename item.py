import random

#add object to hit and decrease health
class Item:
    def __init__(self):
        self.max_speed = 5
        self.selectedItem = random.randint(0,1)
        self.itemArr = ["Jet Booster", "Speed Booster", "Blaster"]
    
    def increaseSpeed(self):
        random_speed = random.randint(0, int(self.max_speed))
        return random_speed
    
    def attack(self):
        random_damage = random.randint(0, 60)
        return random_damage

    def randomItem(self):
        random_item = random.choice(self.itemArr)
        return random_item





