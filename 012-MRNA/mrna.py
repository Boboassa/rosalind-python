# Return number of MRNA sequences that can produce the input protein
# mod 1 000 000

# Define codon number per protein
CODONS = {'A': 4, 'C': 2, 'D': 2, 'E': 2, 'F': 2, 'G': 4, 'H': 2, 'I': 3,
          'K': 2, 'L': 6, 'M': 1, 'N': 2, 'P': 4, 'Q': 2, 'R': 6, 'S': 6,
          'T': 4, 'V': 4, 'W': 1, 'Y': 2, '_': 3}

# Read sequence from file
with open("dataset.txt", "r") as f:
    protein = f.read()[:-1]

# Append stop codon to sequence
protein += '_'
total = 1

for aa in protein:
    total = total * CODONS[aa]
    if total > 1000000:
        total = total % 1000000


print(total)
