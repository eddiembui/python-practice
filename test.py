def main():
    camelcaseinput = input("camelCase: ")
    snake_case = ""
    
    for letter in camelcaseinput:
        # If the letter is uppercase, add an underscore before it
        if letter.isupper():
            snake_case += "_" + letter.lower()
        else:
            snake_case += letter

    print(snake_case)

main()