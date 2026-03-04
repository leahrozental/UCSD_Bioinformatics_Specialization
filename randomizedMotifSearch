import random

def get_profile(motifs, k, t):
    profile = {n: [1.0]*k for n in "ACGT"}
    for m in motifs:
        for i, char in enumerate(m):
            profile[char][i] += 1
    for n in profile:
        for i in range(k):
            profile[n][i] /= (t + 4)
    return profile

def get_most_probable(dna, k, profile):
    max_prob, best_kmer = -1.0, dna[0:k]
    for i in range(len(dna) - k + 1):
        kmer, prob = dna[i:i+k], 1.0
        for j, char in enumerate(kmer):
            prob *= profile[char][j]
        if prob > max_prob:
            max_prob, best_kmer = prob, kmer
    return best_kmer

def get_score(motifs, k, t):
    score = 0
    for i in range(k):
        counts = [m[i] for m in motifs]
        score += (t - counts.count(max(set(counts), key=counts.count)))
    return score

def randomized_motif_search(dna, k, t):
    motifs = [s[i:i+k] for s, i in [(s, random.randint(0, len(s)-k)) for s in dna]]
    best_motifs = motifs
    while True:
        profile = get_profile(motifs, k, t)
        motifs = [get_most_probable(s, k, profile) for s in dna]
        if get_score(motifs, k, t) < get_score(best_motifs, k, t):
            best_motifs = motifs
        else:
            return best_motifs

with open("dataset.txt", "r") as f:
    data = f.read().split()

k, t = int(data[0]), int(data[1])
dna = data[2:]

best_overall = []
min_score = float('inf')

for _ in range(1000):
    res = randomized_motif_search(dna, k, t)
    s = get_score(res, k, t)
    if s < min_score:
        min_score, best_overall = s, res

print("\n".join(best_overall))