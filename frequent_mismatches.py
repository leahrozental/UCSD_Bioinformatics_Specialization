import os
from collections import defaultdict

def HammingDistance(p, q):
    return sum(1 for a, b in zip(p, q) if a != b)

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

def FrequentWordsWithMismatches(Text, k, d):
    counts = defaultdict(int)
    
    for i in range(len(Text) - k + 1):
        pattern = Text[i:i+k]
        for neighbor in neighbors(pattern, d):
            counts[neighbor] += 1
    
    max_count = max(counts.values())
    
    return [p for p, count in counts.items() if count == max_count]

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
    
    result = FrequentWordsWithMismatches(text, k, d)
    print(*(result))

if __name__ == "__main__":
    main()