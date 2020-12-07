import random

#add object to hit and decrease health
class Item:
    def __init__(self, name):
        self.name = name
        self.max_speed = 5
    
    def increaseSpeed(self):
        random_speed = random.randint(0, int(self.max_speed))
        return random_speed



