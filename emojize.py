import emoji

def main():
  emoji_requested = input("Input: ")
  print(f"Output: {emoji.emojize(emoji_requested, language = 'alias')}")



main()