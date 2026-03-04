import random
from collections import Counter

def ProfileWithPseudocounts(Motifs):
    k = len(Motifs[0])
    t = len(Motifs)
    count = {'A': [1.0]*k, 'C': [1.0]*k, 'G': [1.0]*k, 'T': [1.0]*k}
    for motif in Motifs:
        for i, nucleotide in enumerate(motif):
            count[nucleotide][i] += 1
    profile = {nuc: [count[nuc][i] / (t + 4) for i in range(k)] for nuc in "ACGT"}
    return profile

def Score(Motifs):
    if not Motifs: return float('inf')
    k = len(Motifs[0])
    score = 0
    for i in range(k):
        col = [motif[i] for motif in Motifs]
        most_common_count = Counter(col).most_common(1)[0][1]
        score += len(Motifs) - most_common_count
    return score

def Pr(kmer, Profile):
    p = 1.0
    for i, char in enumerate(kmer):
        p *= Profile[char][i]
    return p

def GibbsSampler(Dna, k, t, N):
    Motifs = []
    for string in Dna:
        idx = random.randint(0, len(string) - k)
        Motifs.append(string[idx:idx+k])
    
    BestMotifs = list(Motifs)
    
    for _ in range(N):
        i = random.randint(0, t - 1)
        reduced_motifs = Motifs[:i] + Motifs[i+1:]
        profile = ProfileWithPseudocounts(reduced_motifs)
        
        n = len(Dna[i])
        probs = []
        for j in range(n - k + 1):
            probs.append(Pr(Dna[i][j:j+k], profile))
        
        total = sum(probs)
        if total == 0:
            new_idx = random.randint(0, n - k)
        else:
            weights = [p / total for p in probs]
            new_idx = random.choices(range(n - k + 1), weights=weights)[0]
        
        Motifs[i] = Dna[i][new_idx:new_idx+k]
        
        if Score(Motifs) < Score(BestMotifs):
            BestMotifs = list(Motifs)
            
    return BestMotifs

def main():
    file_path = "dataset.txt"
    
    try:
        with open(file_path, 'r') as f:
            data = f.read().split()
            
        if not data:
            print("file is empty")
            return

        k = int(data[0])
        t = int(data[1])
        N = int(data[2])
        Dna = data[3:]
        
        print(f"Parameters: k={k}, t={t}, N={N}")
        print(f"DNA strings loaded: {len(Dna)}")

        best_overall_motifs = None
        best_overall_score = float('inf')

        num_starts = 20 
        for attempt in range(num_starts):
            current_motifs = GibbsSampler(Dna, k, t, N)
            current_score = Score(current_motifs)
            
            if current_score < best_overall_score:
                best_overall_score = current_score
                best_overall_motifs = current_motifs
            
            print(f"{attempt+1}/{num_starts}, the best score: {best_overall_score}")

        print("\nthe result:")
        print("\n".join(best_overall_motifs))

    except FileNotFoundError:
        print("file dataset.txt not found")

if __name__ == "__main__":
    main()