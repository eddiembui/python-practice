import re

time_in_24hour = {
  "12 AM":"00",
  "1 AM":"01",
  "2 AM":"02",
  "3 AM":"03",
  "4 AM":"04",
  "5 AM":"05",
  "6 AM":"06",
  "7 AM":"07",
  "8 AM":"08",
  "9 AM":"09",
  "10 AM":"10",
  "11 AM":"11",
  "12 PM":"12",
  "1 PM":"13",
  "2 PM":"14",
  "3 PM":"15",
  "4 PM":"16",
  "5 PM":"17",
  "6 PM":"18",
  "7 PM":"19",
  "8 PM":"20",
  "9 PM":"21",
  "10 PM":"22",
  "11 PM":"23"
}

def main():
  print(convert(input("Hours: ")))

def convert(s):
  match = re.search(r"^([0-9]|1[0-2]){1}:?([0-5][0-9])?\s(AM|PM)\sto\s([0-9]|1[0-2]){1}:?([0-5][0-9])?\s(AM|PM)$", s)
  if match:
    time = list(match.groups())
    if time[1] == None:
      time[1] = "00"
    if time[4] == None:
      time[4] = "00"
    
    return f"{time_in_24hour.get(f"{time[0]} {time[2]}")}:{time[1]} to {time_in_24hour.get(f"{time[3]} {time[5]}")}:{time[4]}"
    
  else:
    raise ValueError

if __name__ == "__main__":
  main()