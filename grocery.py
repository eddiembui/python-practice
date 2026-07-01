def main():
  grocery_list = {}
  while True:
    try:
      grocery_item = input("").upper()
      if grocery_item in grocery_list:
        grocery_list[grocery_item] += 1
      else:
        grocery_list.update({grocery_item : 1})
    except(EOFError):
      for keys, values in sorted(grocery_list.items()):
        print(f"{values} {keys}")
      break

    


main()