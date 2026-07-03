import sys
import pyfiglet

def main():
  available_fonts = pyfiglet.Figlet().getFonts()
  if len(sys.argv) == 3:
    if (sys.argv[1] == "-f" or sys.argv[1] == "--font") and (sys.argv[2] in available_fonts):
      user_text = input("Input: ")
      print(f"Output:\n {pyfiglet.figlet_format(user_text, font = sys.argv[2])}")
    else:
      sys.exit("Invalid usage")
  elif len(sys.argv) == 1:
    user_text = input("Input: ")
    print(f"Output:\n {pyfiglet.figlet_format(user_text)}")
  else:
    sys.exit("Invalid usage")


main()
