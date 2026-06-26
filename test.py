def main():
    camelcaseinput = input("camelCase: ")
    uppercaseletters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    uppercaselist = []
    for letter in camelcaseinput:
        for uppercase in uppercaseletters:
            if letter == uppercase: 
                
                uppercaselist.append(letter)
    print(addunderscore(uppercaselist, camelcaseinput))

       
                
def addunderscore(letterlist, originalinput):
    for i in letterlist:
        if i in originalinput:
            originalinput = originalinput.replace(i, f"_{i}")
    return originalinput.lower()


    
main()