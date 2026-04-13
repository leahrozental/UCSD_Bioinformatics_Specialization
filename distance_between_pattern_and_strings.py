import os

def hamming_distance(p, q):
    return sum(1 for a, b in zip(p, q) if a != b)

def distance_between_pattern_and_strings(pattern, dna):
    k = len(pattern)
    distance = 0
    
    for text in dna:
        min_hamming_dist = float('inf')
        
        for i in range(len(text) - k + 1):
            pattern_prime = text[i:i+k]
            current_dist = hamming_distance(pattern, pattern_prime)
            
            if min_hamming_dist > current_dist:
                min_hamming_dist = current_dist
        
        distance += min_hamming_dist
        
    return distance

def main():
    file_name = "dataset.txt"
    if not os.path.exists(file_name):
        print(f" {file_name} not found!")
        return

    with open(file_name, "r") as f:
        pattern = f.readline().strip()
        dna = f.readline().split()

    result = distance_between_pattern_and_strings(pattern, dna)
    print(result)

if __name__ == "__main__":
    main()