import sys
import csv

def main():
  if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
  elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
  elif not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
    sys.exit("File not .csv")

  file_to_open = sys.argv[1]
  try:
    with open(file_to_open) as file:
      data= csv.DictReader(file)  
      with open(sys.argv[2], "w", newline="") as file2:
        writer = csv.DictWriter(file2, fieldnames = ["first","last","house"])
        writer.writeheader()
        for row in data:
          lastname, firstname = row["name"].split(", ")
          writer.writerow({"first": firstname,"last": lastname,"house": row["house"]})

  except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")   


if __name__ == "__main__":
  main()