def main():
    usergreeting = input("Greeting: ")

    # Making usergreeting case-insensitive
    usergreeting = usergreeting.lower()

    # Removing whitespace from usergreeting
    usergreeting = usergreeting.strip()

    print(value(usergreeting))

def value(greeting):
    if "hello" in greeting:
        return "$0"
    elif greeting[0] == "h" and "hello" not in greeting:
        return "$20"
    else:
        return "$100"
if __name__ == "__main__":
    main()