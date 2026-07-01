# user input in x/y format
# x (non-positive integer) and y (positive integer)
# output should be rounded to the nearest integer and in percentage
# if output is 1% or less print E if 99% or higher print F
# if x or y is not an integer or x is greater than y or y is 0 prompt the user again

def main():  
  while True:
    try:
      user_gauge = input("Enter The Gauge Fraction: ")
      index_of_separator = user_gauge.index("/")
      x = int(user_gauge[0:index_of_separator])
      y = int(user_gauge[(index_of_separator + 1):]) 
    except:
      pass
    else:
      if x >= 0 and y >= 1 and x <= y:
        print(checkxy(x,y))
        break
 

  

def checkxy(first, second):  
  gauge_percentage = round((first/second) * 100)
  if gauge_percentage <= 1:
    return "E"
  elif gauge_percentage >= 99:
    return "F"
  else:
    return f"{gauge_percentage}%"


main()