import inflect
p = inflect.engine()
def main():
  names_list = []
  while True:
    try:
      name_input = input("Name: ")
      names_list.append(name_input)
    except(EOFError):
      print(f"Adieu, adieu, to {p.join(names_list)}")
      break
  
main()