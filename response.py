from validator_collection import checkers

def main():
  email_check = checkers.is_email(input("What's your email address: ").strip())
  if email_check == True:
    print("Valid")
  elif email_check == False:
    print("Invalid")
if __name__ == "__main__":
  main()
