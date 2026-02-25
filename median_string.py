import itertools
import os

def HammingDist(p, q):
    return sum(1 for a, b in zip(p, q) if a != b)

def Dist(Pattern, Text):
    k = len(Pattern)
    min_dist = float('inf')
    for i in range(len(Text) - k + 1):
        d = HammingDist(Pattern, Text[i:i+k])
        if d < min_dist:
            min_dist = d
    return min_dist

def MedianString(k, Dna):
    min_total_dist = float('inf')
    best_pattern = ""
    
    for combo in itertools.product("ACGT", repeat=k):
        pattern = "".join(combo)
        current_total_dist = sum(Dist(pattern, seq) for seq in Dna)
        
        if current_total_dist < min_total_dist:
            min_total_dist = current_total_dist
            best_pattern = pattern
            
    return best_pattern

def main():
    file_name = "dataset.txt"
    
    if not os.path.exists(file_name):
        print(f"file {file_name} not found!")
        return

    with open(file_name, "r") as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]
    
    k = int(lines[0])
    dna_list = lines[1:]
    
    if len(dna_list) == 1:
        dna_list = dna_list[0].split()

    result = MedianString(k, dna_list)
    print(result)

if __name__ == "__main__":
    main()