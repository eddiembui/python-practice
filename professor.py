import random

def main():
  user_level = get_level()
  i = 0
  score = 0
  while i < 10:
    x = generate_integer(user_level)
    y = generate_integer(user_level)
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


def get_level():
  while True:
    try:
      level_input = int(input("Level: "))
      if level_input == 1 or level_input == 2 or level_input == 3:

        return level_input

      else:
        print("Input is not in range")

    except ValueError:
      print("Input is a str")




def generate_integer(level):

    if level == 1:
      digit = random.randint(0,9)
    elif level == 2:
      digit = random.randint(10,99)
    elif level == 3:
      digit = random.randint(100,999)
    return digit



if __name__ == "__main__":
  main()
