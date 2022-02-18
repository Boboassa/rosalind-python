# Read a 6 value vector representing the number of couples with different
# genotypes and output the total number of offsprings with the dominant
# phenotype
import numpy as np

# Read the vector
#dataset = np.array([1, 0, 0, 1, 0, 1])
dataset = np.loadtxt("dataset.txt")

# Multiply by number of offspring per couple
OFFSPRING = 2
dataset = dataset * OFFSPRING

# Multiply by the probability of having a dominant phenotype offspring
# AA x AA 1
# AA x Aa 1
# AA x aa 1
# Aa x Aa .75
# Aa x aa .5
# aa x aa 0
PROB = np.array([1, 1, 1, 0.75, 0.5, 0])

final = dataset * PROB

# Sum the different values
total = 0

for num in final:
    total = total + num

print(final)
print(total)
