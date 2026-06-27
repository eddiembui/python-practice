def main():
  userinput = input("Input: ")
  vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
  userinput = list(userinput)
  # loop through userinput list to check if it contains a vowel
  consonants = []
  for letter in userinput:
      if letter not in vowels:
        consonants.append(letter)
        

  consonants = "".join(consonants)
  print(f"Output: {consonants}")

main()