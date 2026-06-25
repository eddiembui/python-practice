distances = {
  "Voyager 1": 132,
  "Voyager 2": 341,
  "Pioneer X": 102,
  "Falcon 9": 0.02
}

def main():
  for name in distances.keys():
    print(f"{name} is {distances[name]} AU from Earth")



main()