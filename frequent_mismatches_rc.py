import os
from collections import defaultdict

def HammingDistance(p, q):
    return sum(1 for a, b in zip(p, q) if a != b)

def ReverseComplement(pattern):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    return "".join(complement[base] for base in reversed(pattern))

def neighbors(pattern, d):
    if d == 0:
        return {pattern}
    if len(pattern) == 1:
        return {'A', 'C', 'G', 'T'}
    
    result = set()
    suffix_neighbors = neighbors(pattern[1:], d)
    for text in suffix_neighbors:
        if HammingDistance(pattern[1:], text) < d:
            for n in 'ACGT':
                result.add(n + text)
        else:
            result.add(pattern[0] + text)
    return result

def FrequentWordsWithMismatchesRC(Text, k, d):
    freq = defaultdict(int)
    
    for i in range(len(Text) - k + 1):
        pattern = Text[i:i+k]
        neighborhood = neighbors(pattern, d)
        for neighbor in neighborhood:
            freq[neighbor] += 1
            freq[ReverseComplement(neighbor)] += 1
            
    if not freq:
        return []
        
    max_freq = max(freq.values())
    return [p for p, count in freq.items() if count == max_freq]

def main():
    if not os.path.exists("dataset.txt"):
        print("not found!")
        return

    with open("dataset.txt", "r") as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]

    if len(lines[0]) > len(lines[1]):
        text, params = lines[0], lines[1].split()
    else:
        text, params = lines[1], lines[0].split()

    k, d = int(params[0]), int(params[1])
    
    print(f"count k={k}, d={d}")
    result = FrequentWordsWithMismatchesRC(text, k, d)
    print("\nanswer:")
    print(*(result))

if __name__ == "__main__":
    main()