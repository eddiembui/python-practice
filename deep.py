useranswer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

# removing white space
useranswer = useranswer.strip()

# adding case-insensitiveness
useranswer = useranswer.lower()


if useranswer == "42" or useranswer == "forty-two" or useranswer == "forty two":
    print("Yes")
else:
    print("No")