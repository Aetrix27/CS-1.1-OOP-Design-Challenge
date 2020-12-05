from powerup import PowerUp

#add object to hit and decrease health
class Item:
    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed
    
    def increaseSpeed(self):
        self.max_speed += 5



