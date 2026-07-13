def main():
  userinput = input("Input: ")
  # loop through userinput list to check if it contains a vowel
  
  print(shorten(userinput))

def shorten(word):
  vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
  word_list = list(word)
  consonants = []
  for letter in word_list:
      if letter not in vowels:
        consonants.append(letter)
        

  consonants = "".join(consonants)
  return f"{consonants}"
   
if __name__ == "__main__":
  main()