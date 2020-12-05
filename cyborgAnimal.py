from racer import Racer
from animal import Animal
from cyborg import Cyborg

class cyborgAnimal(Animal, Cyborg):
    def __init__(self, speed, health, cyborgColor):
        super().__init__(speed, health)
        self.setCyborgColor()
        self.cyborgHealth()


   