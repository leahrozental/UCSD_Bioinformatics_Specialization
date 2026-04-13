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
    
    for Text in SuffixNeighbors:
        if HammingDistance(Pattern[1:], Text) < d:
            for char in "ACGT":
                Neighborhood.add(char + Text)
        else:
            Neighborhood.add(Pattern[0] + Text)
            
    return Neighborhood

def main():
    file_name = "neighbors.txt"
    
    if not os.path.exists(file_name):
        print(f"error: not found {file_name}")
        return

    with open(file_name, "r") as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]
        if len(lines) < 2:
            print("error: 2 lines")
            return
        
        pattern = lines[0]
        d = int(lines[1])

    result = Neighbors(pattern, d)

    print("\n".join(result))

if __name__ == "__main__":
    main()