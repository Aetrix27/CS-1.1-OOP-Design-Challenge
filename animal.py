from racer import Racer

class Animal(Racer):
    def __init__(self, speed, health):
        super().__init__(speed, health)
        self.animalSpeed()
        self.setAnimal()

    def animalSpeed(self):
      self.speed += 10

    def setAnimal(self):
        self.animal= input("What animal do you want to be?")
