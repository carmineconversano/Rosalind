file = open("rosalind_dna.txt", "r")
nucleotidelist = file.read()

def countNucleotide(character, string):
    count = 0
    for i in string:
        if i == character:
            count = count + 1

    print(str(count), end = ' ')

dnaAlphabet = ["A", "C", "G", "T"]

for dna in dnaAlphabet:
    countNucleotide(dna, nucleotidelist)

print("")
