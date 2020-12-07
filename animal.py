from racer import Racer

class Animal(Racer):
    def __init__(self):
        self.health = 100
        self.speed = 35
        super().__init__(self.health, self.speed)
        self.setAnimalSpecies()

    def setAnimalSpecies(self):
      self.animal = input("What animal species do you want to be?")
      print(f"You are a {self.animal}")



