from animal import Animal
from cyborg import Cyborg

class CyborgAnimal(Animal, Cyborg):
    def __init__(self, animal, cyborgColor):
        self.health = 105
        self.speed = 32.5
        self.animal = animal
        self.cyborgColor = cyborgColor
   

   