from racer import Racer

class Cyborg(Racer):
   def __init__(self, isPlayer, name):
      health = 110
      speed = 30
      name = name
      self.cyborgColor = ""
      self.isPlayer = isPlayer
      super().__init__(health, speed, name)

      if self.isPlayer == True:
         self.setCyborgColor()
      else:
         self.cyborgColor = "Purple"
         
   def setCyborgColor(self):
      self.cyborgColor = input("What do you want your cyborg color to be?\n")
      print(f"You are a {self.cyborgColor} colored cyborg\n")






