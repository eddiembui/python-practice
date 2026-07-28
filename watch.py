import re

def main():
  print(parse(input("HTML: ")))

def parse(link):
  pattern = re.search(r'^<iframe\s.*\s?src="(?:http://|https://)(?:youtube\.com/|www\.youtube\.com/)embed/([a-zA-Z0-9_-]+)"(?:\s.*)?></iframe>$', link)
  if pattern:
    return f"https://youtu.be/{pattern.group(1)}"
  else:
    return None

if __name__ == "__main__":
  main()
