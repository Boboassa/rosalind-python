# Given a protein string return its mass

# Open file
with open("dataset.txt", "r") as f:
    protein = f.read()[:-1]

# Molecular mass of each aminoacid
aaMass = {
    "A": 71.03711,  "C": 103.00919, "D": 115.02694, "E": 129.04259,
    "F": 147.06841, "G": 57.02146,  "H": 137.05891, "I": 113.08406,
    "K": 128.09496, "L": 113.08406, "M": 131.04049, "N": 114.04293,
    "P": 97.05276,  "Q": 128.05858, "R": 156.10111, "S": 87.03203,
    "T": 101.04768, "V": 99.06841,  "W": 186.07931, "Y": 163.06333 }

# Creates a list of elements and then sums them
#mass = round((sum([aaMass[aa] for aa in protein])), 3)

# Computes each element and sums it without creating a list
mass = round((sum(aaMass[aa] for aa in protein)), 3)

# Print result
print(mass)
