from racer import Racer

class Animal(Racer):
    def __init__(self, isPlayer, name):
        health = 100
        speed = 35
        name = name
        self.animal = ""
        self.isPlayer = isPlayer
        super().__init__(health, speed, name)

        if self.isPlayer == True:
            self.setAnimalSpecies()
        else:
            self.animal = "Lion"

    def setAnimalSpecies(self):
      self.animal = input("What animal species do you want to be?\n")
      print(f"You are a {self.animal}\n")
    
    



