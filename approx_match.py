def HammingDistance(p, q):
    return sum(1 for i in range(len(p)) if p[i] != q[i])

def ApproximatePatternMatching(Pattern, Text, d):
    positions = []
    k = len(Pattern)
    for i in range(len(Text) - k + 1):
        substring = Text[i:i+k]
        if HammingDistance(Pattern, substring) <= d:
            positions.append(i)
    return positions

try:
    with open("dataset.txt", "r") as f:
        lines = f.read().splitlines()
        pattern = lines[0].strip()
        text = lines[1].strip()
        d = int(lines[2].strip())
        
        result = ApproximatePatternMatching(pattern, text, d)
        
        print(*(result))
except FileNotFoundError:
    print("FileNotFoundError")