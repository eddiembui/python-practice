import sys

def main():
  if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
  elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

  argument = sys.argv[1]
  try:
    index_of_period = argument.index(".")
    if argument[(index_of_period + 1): ] != "py":
      sys.exit("Not a python file")
  except ValueError:
    sys.exit("Not a python file")
  
  code_lines = 0
  try:
    with open(argument) as file:
      for line in file:
        line = line.strip()
        if line.startswith("#") or line == "":
          code_lines += 0
        else:
          code_lines += 1
        
    print(code_lines)

  except FileNotFoundError:
    sys.exit("File does not exist")

  

if __name__ == "__main__":
  main()