import random

def main():
  while True:
    try:
      number_entered = input("Level: ")
      if int(number_entered) > 0:
        number_generated = random.randint(1, int(number_entered))
        check_guess(number_generated)
        break
    except(ValueError):
      pass

def check_guess(theguess):
  while True:
    try:
      user_guess = input("Guess: ")
      if int(user_guess) > 0:
        if int(user_guess) > theguess:
          print("Too large")
        elif int(user_guess) < theguess:
          print("Too small")
        else:
          print("Just right")
          break
          
    except(ValueError):
      pass
    

main()