
def main():
    usertime = input("What time is it? ")
    constanttime = convert(usertime)
    if constanttime >= 7.0 and constanttime <= 8.0:
        print("breakfast time")
    elif constanttime >= 12.0 and constanttime <= 13.0:
        print("lunch time")
    elif constanttime >= 18.0 and constanttime <= 19.0:
        print("dinner time")

def convert(time):
    separatorindex = time.find(":")
    hour = float(time[0:separatorindex])
    minute = int(time[separatorindex + 1:])
    minutetohour = minute/60
    newhour = hour + minutetohour
    constanttime = float(newhour)
    return constanttime


if __name__ == "__main__":
    main()