f = open("rosalind_revc.txt", "r")
DNA = f.read()[::-1]

for char in DNA:
    if(char == "A"):
        print("T", sep='', end='')
    elif (char == "T"):
        print("A", sep='', end='')
    elif (char == "C"):
        print("G", sep='', end='')
    elif (char == "G"):
        print("C", sep='', end='')

print('')

