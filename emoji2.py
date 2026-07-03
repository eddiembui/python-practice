constanttime = 0
def main():
    usertime = input("What time is it? ")
    convert(usertime)
    if constanttime >= 7.0 and constanttime <= 8.0:
        print("breakfast time")
    elif constanttime >= 12.0 and constanttime <= 13.0:
        print("lunch time")
    elif constanttime >= 18.0 and constanttime <= 19.0:
        print("dinner time")

def convert(time):
    global constanttime
    separatorindex = time.find(":")
    hour = float(time[0:separatorindex])
    
    firstperiod = time.find(".")
    minute = int(time[separatorindex + 1: firstperiod - 2])
    if hour == 12.0 and time[firstperiod - 1] == "p":
        minute = minute/60
        constanttime = float(hour + minute)
    elif time[firstperiod - 1] == "a" and hour != 12.0:
        minute = minute/60
        constanttime = float(hour + minute)
    elif time[firstperiod - 1] == "p":
        hour = hour + 12
        minute = minute/60
        constanttime = float(hour + minute)
    return constanttime


if __name__ == "__main__":
    main()
