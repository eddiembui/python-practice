import sys
from tabulate import tabulate

def main():
  if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
  elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

  argument = sys.argv[1]
  try:
    index_of_period = argument.index(".")
    if argument[(index_of_period + 1): ] != "csv":
      sys.exit("Not a CSV file")
  except ValueError:
    sys.exit("Not a CSV file")
  
  table = []
  try:
    with open(argument) as file:
      for line in file:
        table.append(line.rstrip().split(","))
        
      print(tabulate(table, headers = "firstrow", tablefmt = "grid"))

  except FileNotFoundError:
    sys.exit("File does not exist")

if __name__ == "__main__":
  main()