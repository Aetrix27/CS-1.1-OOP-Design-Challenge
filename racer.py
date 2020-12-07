from powerup import PowerUp
from item import Item

class Racer:
    def __init__(self, health=100):
        self.speed = 30
        self.health = health
        self.boosts = list()
        self.items = list()

    def speak(self, message):
        print(message)

    def getPowerUp(self, powerUp):
        self.boosts.append(powerUp)

    def addItem(self, item):
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

def checkWinner(self, racer1, racer2):
    if racer1.speed > 100 and racer1.speed > racer2.speed:
        print("Racer1 wins!")
    elif racer2.speed > 100 and racer2.speed > racer1.speed:
        print("Racer 2 wins!")
    elif racer1.speed == racer2.speed:
        print("It's a tie!")
            #gameRunning=false

#while gameRunning == true
#powerUp1 = PowerUp("Speed", 100)
item1 = Item("Booster")
racer1 = Racer()
racer1.addItem(item1)
print(racer1.totalBoost())
print(racer1.speed)

print(racer1.totalPowerUp())
powerup1 = PowerUp("Booma")
racer1.getPowerUp(powerup1)
print(racer1.totalPowerUp())
