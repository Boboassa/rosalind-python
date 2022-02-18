# Read a 6 value vector representing the number of couples with different
# genotypes and output the total number of offsprings with the dominant
# phenotype

# Define number of offspring per couple
OFFSPRING = 2

# Define probability of dominant offspring as:
# AA x AA = 1
# AA x Aa = 1
# AA x aa = 1
# Aa x Aa = 0.75
# Aa x aa = 0.5
# aa x aa = 0
PROB = [1, 1, 1, 0.75, 0.5, 0]

# Read the vector
with open("dataset.txt", "r") as f:
    dataset = [int(x) for x in f.read().split()]

# Multiply by number of offspring per couple
dataset = [a * OFFSPRING for a in dataset]

# Multiply by the probability of having a dominant phenotype offspring
# and sum the different values
total = sum([a*b for a, b in zip(dataset, PROB)])

# Print result
print(total)
