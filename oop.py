class Microwave:
  def __init__(self,brand,power_rating):
    self.brand = brand
    self.power_rating = power_rating
    self.turned_on = False

  def turn_on(self):
    if self.turned_on:
      print(f"{self.brand} is already turned on")
    else:
      self.turned_on = True
      print(f"{self.brand} turned on")

  def turn_off(self):
    if self.turned_on:
      self.turned_on = False
      print(f"{self.brand} has been turned off")
    else:
      print(f"{self.brand} is already off")

  def run(self,seconds: int):
    if self.turned_on:
      print(f"{self.brand} is running for {seconds} seconds")
    else:
      print(f"Turn on your {self.brand} microwave first...")

smeg = Microwave("Smeg","B")
smeg.turn_on()
smeg.turn_on()
smeg.run(5)
smeg.turn_off()
smeg.run(6)

ramtons = Microwave("Ramtons","C")
