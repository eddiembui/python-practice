import re

def main():
  print(validate(input("What's your IP Address: ")))


def validate(ip):
  octet = r"(?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])"
  pattern = rf"^{octet}\.{octet}\.{octet}\.{octet}$"
  return bool(re.match(pattern, ip))


if __name__ == "__main__":
  main()
  