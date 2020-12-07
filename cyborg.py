from racer import Racer

class Cyborg(Racer):
   def __init__(self, isPlayer):
      self.health = 100
      self.speed = 30
      self.isPlayer = isPlayer
      super().__init__(self.health, self.speed)
      self.cyborgHealth()

      if self.isPlayer == True:
         self.setCyborgColor()
      else:
         self.cyborgColor = "Purple"

   def setCyborgColor(self):
      self.cyborgColor = input("What do you want your cyborg color to be?")
      print(f"You are a {self.cyborgColor} colored cyborg")

   def cyborgHealth(self):
      self.health += 10




