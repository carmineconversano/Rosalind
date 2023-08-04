RNA = open("rosalind_prot.txt", "r").read()
numberOfProteins = len(RNA)


class Protein:
    def __init__(self, proteinLetter, arrayOfRnaString):
        self.proteinLetter = proteinLetter
        self.arrayOfRnaString = arrayOfRnaString


def findAmmino(ammino):
    F = ["UUU", "UUC"]
    L = ["UUA", "UUG", "CUU", "CUC", "CUA", "CUG"]
    S = ["UCU", "UCC", "UCA", "UCG", "AGU", "AGC"]
    Y = ["UAU", "UAC"]
    STOP = ["UAA", "UAG", "UGA"]
    C = ["UGU", "UGC"]
    W = ["UGG"]
    P = ["CCU", "CCC", "CCA", "CCG"]
    H = ["CAU", "CAC"]
    Q = ["CAA", "CAG"]
    R = ["CGU", "CGC", "CGA", "CGG", "AGA", "AGG"]
    I = ["AUU", "AUC", "AUA"]
    M = ["AUG"]
    T = ["ACU", "ACC", "ACA", "ACG"]
    N = ["AAU", "AAC"]
    K = ["AAA", "AAG"]
    V = ["GUU", "GUC", "GUA", "GUG"]
    A = ["GCU", "GCC", "GCA", "GCG"]
    D = ["GAU", "GAC"]
    E = ["GAA", "GAG"]
    G = ["GGU", "GGC", "GGA", "GGG"]

    proteins = [Protein("F", F), Protein("L", L), Protein("S", S), Protein("Y", Y), Protein("STOP", STOP), Protein("C", C), Protein("W", W), Protein(
        "P", P), Protein("H", H), Protein("Q", Q), Protein("R", R), Protein("I", I), Protein("M", M), Protein("T", T), Protein("N", N), Protein("K", K), Protein("V", V), Protein("A", A), Protein("D", D), Protein("E", E), Protein("G", G)]

    for p in proteins:
        if(ammino in p.arrayOfRnaString):
            if(p.proteinLetter != "STOP"):
                return p.proteinLetter

    return ""


for i in range(numberOfProteins):
    ammino = RNA[i*3:(i*3)+3]
    print(findAmmino(ammino), sep='', end='')

print("")
