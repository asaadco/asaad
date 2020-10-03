# 4.2 How Do Bacteria Make Antibiotics?
# Peptide Encoding Problem: Find substrings of a genome encoding a given amino acid sequence.
from Ex1 import translate, constructGeneticCode

def findPeptideEncoders(DNA, Peptide, geneticCode):
    '''
    :params DNA: text string DNA
    :params Peptide: required pattern Peptide to look for
    :params geneticCode: genetic code translation from RNA to DNA
    :return: Peptide Encoders from DNA
    '''
    encoders = []
    translation = ""
    k = len(Peptide)*3
    for i in range(0, len(DNA)-k+1):
        pattern = DNA[i:i+k].replace("T", "U")
        rpattern = reverseComplement(DNA[i:i+k]).replace("T", "U")
        translation = translate(pattern, geneticCode)
        rtranslation = translate(rpattern, geneticCode)
        if translation == Peptide or rtranslation == Peptide:
            encoders.append(DNA[i:i+k])
    
    return encoders


def reverseComplement(pattern):
    # Input: A DNA string Pattern.
    # Output: Patternrc , the reverse complement of Pattern.
    DNAmap = {"A":"T", "T":"A", "G":"C", "C":"G",}  # For mapping translation
    rcPattern = ""
    for i in range(len(pattern)-1, -1, -1): # Start from the end of the string, range(START, END, INCREMENT).
        # The loop terminates immediately when i == -1
        rcPattern = rcPattern + (DNAmap.get(pattern[i]))
    return rcPattern

if __name__ == "__main__":
    geneticCode = constructGeneticCode()
    with open("Bacillus_brevis.txt") as dataset:
        genome = dataset.read().strip()
        # print("\n".join((findPeptideEncoders(genome.strip().replace("\n", ""), "VKLFPWFNQ", geneticCode))))
        print(len(findPeptideEncoders(genome.strip().replace("\n", ""), "VKLFPWFNQ", geneticCode)))
