from racer import Racer

class Cyborg(Racer):
   cyborgColor = ""
   def __init__(self, speed, health, cyborgColor):
      super().__init__(speed, health)
      self.setCyborgColor()
      self.cyborgHealth()
   
   def setCyborgColor(self):
      self.cyborgColor = input("What do you want your cyborg color to be?")
      print(f"You are a {self.cyborgColor} colored cyborg")

   def cyborgHealth(self):
      self.health += 10




