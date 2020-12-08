from racer import Racer

class Cyborg(Racer):
   def __init__(self, isPlayer, name):
      self.health = 110
      self.speed = 30
      self.isPlayer = isPlayer
      self.name = name
      
      super().__init__(self.health, self.speed, self.name)

      if self.isPlayer == True:
         self.setCyborgColor()
      else:
         self.cyborgColor = "Purple"

   def returnSpeed(self):
      return f"The speed of {self.name} is now {self.speed}"

   def setCyborgColor(self):
      self.cyborgColor = input("What do you want your cyborg color to be?")
      print(f"You are a {self.cyborgColor} colored cyborg")






