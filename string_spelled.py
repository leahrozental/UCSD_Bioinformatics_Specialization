with open('dataset.txt', 'r') as f:
    kmers = f.read().split()

genome = kmers[0]

for i in range(1, len(kmers)):
    genome += kmers[i][-1]

print(genome)
