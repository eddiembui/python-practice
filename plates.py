import string
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
 

  # loops through the punctuation marks and checks if any of them are in the str
  for i in string.punctuation:
    if i in s:
      return False
  firstnumberindex = None

  # this loop gets the index of the first number in the str
  for j in s:
    if j.isnumeric():
      firstnumberindex = s.index(j)
      break
  """
    checks if the str ends in numeric from the initial numeric and also if that first number is not a 0 and if the first 2 two characters are alphabets
    and check if the length is a minimum of 2 and a maximum of 6 and there's no space in the str
  """
  if s[firstnumberindex:].isnumeric() and s[firstnumberindex] != "0" and s[0:2].isalpha() and 2 <= len(s) <= 6 and " " not in s:
    return True
  elif firstnumberindex == None and 2 <= len(s) <= 6 and " " not in s:
    return True
  else:
    return False  
  

  

if __name__ == "__main__":
  main()