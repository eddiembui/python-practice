def main():
    camelcaseinput = input("camelCase: ")
    uppercaseletters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    indexes = []
    for letter in camelcaseinput:
        for uppercase in uppercaseletters:
            if letter == uppercase: 
                indexofuppercase = camelcaseinput.index(letter)
                indexes.append(indexofuppercase)
    print(addunderscore(indexes, camelcaseinput))

       
                
def addunderscore(nmbr, originalinput):
    originalinput = list(originalinput)
    for i in nmbr:
        originalinput.insert(i, "_")        
        print(i)
    snakecase = "".join(originalinput)
    print(snakecase)



    
main()