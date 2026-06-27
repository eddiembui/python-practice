import string
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
  y = True

  # checks if the first 2 letters are alphabets, minimum characters are 2 and maximum characters are 6, a space is not in the str
  if s[0:2].isalpha() and 2 <= len(s) <= 6 and " " not in s :
    y = True
  else:
    y = False

  # loops through the punctuation marks and checks if any of them are in the str
  for i in string.punctuation:
    if i in s:
      y = False
  firstnumberindex = 0

  # this loop gets the index of the first number in the str
  for j in s:
    if j.isnumeric():
      firstnumberindex = s.index(j)
      break
  
  # checks if the str ends in numeric from the initial numeric and also if that first number is not a 0
  if s[firstnumberindex:].isnumeric() and s[firstnumberindex] != "0":
    y = True
  else:
    y = False  


  return y


main()