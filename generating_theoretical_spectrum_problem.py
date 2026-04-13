def get_amino_acid_mass():
    return {
        'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99, 'T': 101, 'C': 103, 'I': 113,
        'L': 113, 'N': 114, 'D': 115, 'K': 128, 'Q': 128, 'E': 129, 'M': 131,
        'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186
    }

def solve_cyclospectrum(filename):
    with open(filename, 'r') as f:
        peptide = f.read().strip()
    
    mass_table = get_amino_acid_mass()
    n = len(peptide)
    
    prefix_mass = [0] * (n + 1)
    for i in range(n):
        prefix_mass[i+1] = prefix_mass[i] + mass_table[peptide[i]]
    
    total_mass = prefix_mass[n]
    spectrum = [0]
    
    for length in range(1, n):
        for start in range(n):
            if start + length <= n:
                sub_mass = prefix_mass[start + length] - prefix_mass[start]
            else:
                
                sub_mass = total_mass - (prefix_mass[start] - prefix_mass[start + length - n])
            spectrum.append(sub_mass)
    
    spectrum.append(total_mass)
    
    print(*(sorted(spectrum)))

solve_cyclospectrum('dataset.txt')