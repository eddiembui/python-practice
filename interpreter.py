def main():
    userinput = input("Expression: ")
    firstspace = userinput.find(" ")
    secondspace = firstspace + 2
    firstint = float(userinput[0:firstspace])
    operator = userinput[firstspace + 1]
    secondint = float(userinput[secondspace + 1:])

    print(calculation(firstint, operator, secondint))


def calculation(int1, operationsign, int2):
    operation = 0
    if operationsign == "+" :
        operation = int1 + int2
    elif operationsign == "-":
        operation = int1 - int2
    elif operationsign == "*":
        operation = int1 * int2
    else:
        operation = int1 / int2
    return round(operation, 1)

main()