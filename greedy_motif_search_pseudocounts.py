import os

def count_with_pseudocounts(motifs):
    k = len(motifs[0])
    count = {symbol: [1] * k for symbol in "ACGT"}
    for motif in motifs:
        for i, symbol in enumerate(motif):
            count[symbol][i] += 1
    return count

def profile_with_pseudocounts(motifs):
    t = len(motifs)
    k = len(motifs[0])
    count = count_with_pseudocounts(motifs)
    profile = {symbol: [c / (t + 4) for c in count[symbol]] for symbol in "ACGT"}
    return profile

def score(motifs):
    k = len(motifs[0])
    t = len(motifs)
    count = {symbol: [0] * k for symbol in "ACGT"}
    for motif in motifs:
        for i, symbol in enumerate(motif):
            count[symbol][i] += 1
            
    res = 0
    for j in range(k):
        max_count = max(count[symbol][j] for symbol in "ACGT")
        res += (t - max_count)
    return res

def profile_most_probable(text, k, profile):
    max_prob = -1.0
    best_kmer = text[0:k]
    for i in range(len(text) - k + 1):
        kmer = text[i:i+k]
        prob = 1.0
        for j, symbol in enumerate(kmer):
            prob *= profile[symbol][j]
        if prob > max_prob:
            max_prob = prob
            best_kmer = kmer
    return best_kmer

def greedy_motif_search_with_pseudocounts(dna, k, t):
    best_motifs = [seq[0:k] for seq in dna]
    n = len(dna[0])
    
    for i in range(n - k + 1):
        motifs = [dna[0][i:i+k]]
        for j in range(1, t):
            current_profile = profile_with_pseudocounts(motifs)
            motifs.append(profile_most_probable(dna[j], k, current_profile))
            
        if score(motifs) < score(best_motifs):
            best_motifs = motifs
            
    return best_motifs

def main():
    file_name = "dataset.txt"
    if not os.path.exists(file_name):
        return

    with open(file_name, "r") as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]

    k, t = map(int, lines[0].split())
    dna = lines[1:]
    if len(dna) == 1:
        dna = dna[0].split()

    result = greedy_motif_search_with_pseudocounts(dna, k, t)
    print("\n".join(result))

if __name__ == "__main__":
    main()