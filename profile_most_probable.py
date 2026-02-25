import os

def kmer_probability(kmer, profile):
    prob = 1.0
    nucleotides = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    for i, nucleotide in enumerate(kmer):
        prob *= profile[nucleotides[nucleotide]][i]
    return prob

def find_most_probable(text, k, profile):
    max_prob = -1.0 
    best_kmer = text[0:k] 

    for i in range(len(text) - k + 1):
        kmer = text[i:i+k]
        prob = kmer_probability(kmer, profile)
        
        
        if prob > max_prob:
            max_prob = prob
            best_kmer = kmer
            
    return best_kmer

def main():
    file_name = "dataset.txt"
    if not os.path.exists(file_name):
        print("not found!")
        return

    with open(file_name, "r") as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]

    text = lines[0]
    k = int(lines[1])
    
    profile = []
    for i in range(2, 6):
        row = list(map(float, lines[i].split()))
        profile.append(row)

    result = find_most_probable(text, k, profile)
    print(result)

if __name__ == "__main__":
    main()