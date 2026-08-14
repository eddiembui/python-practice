from datetime import date
import operator
import inflect
import sys

p = inflect.engine()
def main():
  user_date = input("Enter date (YYYY-MM-DD): ")
  try:
    year, month, day = user_date.split("-")
    x = date(int(year),int(month),int(day))
    print(convert_to_minutes(x))
    
    
  except ValueError:
    sys.exit("Wrong format!")

# used during testing
def date_format(date_str):
  try:
    year, month, day = date_str.split("-")
    return convert_to_minutes(date(int(year), int(month), int(day)))
  except ValueError:
    sys.exit("Wrong format!")

def convert_to_minutes(date_given):
  if date_given > date.today():
    sys.exit("Enter a historical date")
  elif date_given == date.today():
    return "0 minutes difference"
  else:  
    days_diff = operator.sub(date.today(), date_given)
    
    days, _useless = str(days_diff).split(", ")
    int_days, _caption = days.split()
    minutes_diff = ((int(int_days) * 24) * 60) 
    return f"{p.number_to_words(minutes_diff).capitalize().replace(" and", "")} minutes"
    
if __name__ == "__main__":
  main()