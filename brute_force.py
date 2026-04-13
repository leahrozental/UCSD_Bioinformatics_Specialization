import os

def HammingDistance(p, q):
    return sum(1 for a, b in zip(p, q) if a != b)

def Neighbors(Pattern, d):
    if d == 0:
        return {Pattern}
    if len(Pattern) == 1:
        return {'A', 'C', 'G', 'T'}
    
    Neighborhood = set()
    SuffixNeighbors = Neighbors(Pattern[1:], d)
    for text in SuffixNeighbors:
        if HammingDistance(Pattern[1:], text) < d:
            for char in "ACGT":
                Neighborhood.add(char + text)
        else:
            Neighborhood.add(Pattern[0] + text)
    return Neighborhood


def MotifEnumeration(Dna, k, d):
    patterns = set()
    all_possible_motifs = set()
    
    for seq in Dna:
        for i in range(len(seq) - k + 1):
            kmer = seq[i:i+k]
            all_possible_motifs.update(Neighbors(kmer, d))
    

    for candidate in all_possible_motifs:
        match_in_all_strings = True
        
        for seq in Dna:
            found_in_current_seq = False
            for i in range(len(seq) - k + 1):
                if HammingDistance(candidate, seq[i:i+k]) <= d:
                    found_in_current_seq = True
                    break
            
           
            if not found_in_current_seq:
                match_in_all_strings = False
                break
        
        if match_in_all_strings:
            patterns.add(candidate)
            
    return patterns


def main():
    file_name = "dataset.txt"
    if not os.path.exists(file_name):
        print(f"file {file_name} not found!")
        return

    with open(file_name, "r") as f:
        line1 = f.readline().split()
        if not line1: return
        k, d = int(line1[0]), int(line1[1])
        
        dna_list = f.readline().split()

    result = MotifEnumeration(dna_list, k, d)
    
    print(" ".join(sorted(result)))

if __name__ == "__main__":
    main()