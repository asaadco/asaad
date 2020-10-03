# 4.11 CS: Generating the Theoretical Spectrum of a Peptide

def LinearSpectrum(Peptide, AminoAcidMass):
    prefixMass = [0]*(len(Peptide)+1)
    for i in range(1, len(prefixMass)):
        prefixMass[i] = (prefixMass[i-1] + int(AminoAcidMass[Peptide[i-1]]))
    LinearSpectrum = [0]
    for i in range(len(Peptide)-1):
        for j in range(i+1, len(Peptide)+1):
            print(i, j)
            LinearSpectrum.append(prefixMass[j%len(Peptide)] - prefixMass[i])
    return sorted(LinearSpectrum)

def constructAminoAcidMass():
    AminoDict = {}
    with open("integer_mass_table.txt") as aminoAcid:
        codes = aminoAcid.readlines()
        for code in codes:
            code = code.split(" ")
            AminoDict[code[0]] = code[1].strip()
    return AminoDict


if __name__ == "__main__":
    AminoAcidMass = constructAminoAcidMass()
    print(AminoAcidMass)
    print(LinearSpectrum("NQEL", AminoAcidMass))
