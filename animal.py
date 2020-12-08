from racer import Racer

class Animal(Racer):
    def __init__(self, isPlayer, name):
        self.health = 100
        self.speed = 35
        self.name = name
        self.animal = ""
        super().__init__(self.health, self.speed, self.name)
        self.isPlayer = isPlayer

        if self.isPlayer == True:
            self.setAnimalSpecies()
        else:
            self.animal = "Lion"

    def returnSpeed(self):
      return f"The speed of {self.name} is now {self.speed}"
    
    def setAnimalSpecies(self):
      self.animal = input("What animal species do you want to be?")
      print(f"You are a {self.animal}")



