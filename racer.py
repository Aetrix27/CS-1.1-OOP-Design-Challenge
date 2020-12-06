from powerup import PowerUp

class Racer:
    def __init__(self, speed, health=100):
        self.speed = 0
        self.health = health
        self.boosts = list()

    def speak(self, message):
        print(message)

    def getPowerUp(self, powerUp):
        self.boosts.append(powerUp)

powerUp1 = PowerUp("Speed", 100)
