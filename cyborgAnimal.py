from animal import Animal
from cyborg import Cyborg

class CyborgAnimal(Animal, Cyborg):
    def __init__(self, isPlayer, name):
        self.health = 105
        self.speed = 32.5
        self.name = name 
        self.isPlayer = isPlayer
        self.boosts = list()
        self.items = list()

        if self.isPlayer == True:
            self.setCyborgColor()
        else:
            self.cyborgColor = "Purple"

        if self.isPlayer == True:
            self.setAnimalSpecies()
        else:
            self.animal = "Lion"


   