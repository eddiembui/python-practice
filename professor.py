import random 

def main():
  get_level()
  

def get_level():
  while True:
    try:
      level_input = int(input("Level: "))
      if level_input == 1 or level_input == 2 or level_input == 3:
        generate_integer(level_input)
        break
      else:
        print("Input is not in range")
        
    except ValueError:
      print("Input is a str")
      
    


def generate_integer(level):
  i = 0
  score = 0
  while i < 10:
    if level == 1:
      x = random.randint(0,6)
      y = random.randint(0,6)
    elif level == 2:
      x = random.randint(7,12)
      y = random.randint(7,12)
    elif level == 3:
      x = random.randint(13,18)
      y = random.randint(13,18)

    wrong_attempts = 0
    while wrong_attempts != 3:
      try:
        user_answer = int(input(f"{x} + {y} = "))
        sum_answer = x + y
        if user_answer != sum_answer:
          print("EEE")
          wrong_attempts += 1
          
        elif user_answer == sum_answer:
          score += 1
          break
      except ValueError:
        print("EEE")
        wrong_attempts += 1
        
    else:
      print(f"{x} + {y} = {sum_answer}")
      
    i += 1
  else:
    print(f"Score: {score}")
  


main()