months = [
  "January",
  "February",
  "March",
  "April",
  "May",
  "June",
  "July",
  "August",
  "September",
  "October",
  "November",
  "December"
]

def main():
  while True:
    date_entered = input("Date: ").strip()
    if "/" in date_entered:
      separated_list = date_entered.split("/")
      month = (separated_list[0])
      day = (separated_list[1])
      if month.isdigit() and day.isdigit():
        if int(month) <= 12 and int(day) <= 31:
          if int(month) < 10 and int(day) < 10:
            print(f"{separated_list[2]}-0{separated_list[0]}-0{separated_list[1]}")
          elif int(day) < 10:
            print(f"{separated_list[2]}-{separated_list[0]}-0{separated_list[1]}")
          elif int(month) < 10:
            print(f"{separated_list[2]}-0{separated_list[0]}-{separated_list[1]}")
          else:
            print(f"{separated_list[2]}-{separated_list[0]}-{separated_list[1]}")
          break
    elif "," in date_entered:
      separated_list = date_entered.split(",")
      month_and_date = separated_list[0].split(" ")
      month = month_and_date[0]
      day = month_and_date[1]
      year = separated_list[1].strip()
      if month in months and int(day) <= 31 and date_entered[date_entered.index(",") + 1 == " "] and day.isdigit():
        if (months.index(month) + 1) < 10 and int(day) < 10:
          print(f"{year}-0{months.index(month) + 1}-0{day}")
        elif (months.index(month) + 1) < 10:
          print(f"{year}-0{months.index(month) + 1}-{day}")
        elif int(day) < 10:
          print(f"{year}-{months.index(month) + 1}-0{day}")
        else:
          print(f"{year}-{months.index(month) + 1}-{day}")
        break



main()