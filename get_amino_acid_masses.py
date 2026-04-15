import os

def get_amino_acid_masses():
    return [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]

def get_linear_spectrum(peptide):
    prefix_mass = [0]
    for m in peptide:
        prefix_mass.append(prefix_mass[-1] + m)
    spec = [0]
    for i in range(len(peptide)):
        for j in range(i + 1, len(peptide) + 1):
            spec.append(prefix_mass[j] - prefix_mass[i])
    return sorted(spec)

def get_cyclic_spectrum(peptide):
    prefix_mass = [0]
    for m in peptide:
        prefix_mass.append(prefix_mass[-1] + m)
    total_mass = prefix_mass[-1]
    spec = [0]
    for i in range(len(peptide)):
        for j in range(i + 1, len(peptide) + 1):
            spec.append(prefix_mass[j] - prefix_mass[i])
            if i > 0 and j < len(peptide):
                spec.append(total_mass - (prefix_mass[j] - prefix_mass[i]))
    return sorted(spec)

def is_consistent(peptide, spectrum_counts):
    l_spec = get_linear_spectrum(peptide)
    l_counts = {}
    for m in l_spec:
        l_counts[m] = l_counts.get(m, 0) + 1
    for m, count in l_counts.items():
        if spectrum_counts.get(m, 0) < count:
            return False
    return True

def solve():
    file_path = 'dataset.txt'
    
    if not os.path.exists(file_path):
        print(f"file {file_path} not found!")
        print(f"current foulder: {os.getcwd()}")
        return

    with open(file_path, 'r') as f:
        data = f.read().split()
    
    if not data:
        print("file is empty!")
        return
        
    spectrum = sorted([int(x) for x in data])
    parent_mass = max(spectrum)
    
    spectrum_counts = {}
    for m in spectrum:
        spectrum_counts[m] = spectrum_counts.get(m, 0) + 1

    amino_masses = get_amino_acid_masses()
    candidates = [[]]
    final_peptides = set()

    while candidates:
        new_candidates = []
        for peptide in candidates:
            for mass in amino_masses:
                new_candidates.append(peptide + [mass])
        
        candidates = []
        for peptide in new_candidates:
            current_mass = sum(peptide)
            if current_mass == parent_mass:
                if get_cyclic_spectrum(peptide) == spectrum:
                    final_peptides.add("-".join(map(str, peptide)))
            elif current_mass < parent_mass:
                if is_consistent(peptide, spectrum_counts):
                    candidates.append(peptide)
    
    print(*(final_peptides))

if __name__ == "__main__":
    solve()