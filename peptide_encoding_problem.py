def reverse_complement(dna):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    return "".join(complement.get(base, base) for base in reversed(dna))

def dna_to_rna(dna):
    return dna.replace('T', 'U')

def translate_rna(rna, genetic_code):
    peptide = ""
    for i in range(0, len(rna), 3):
        codon = rna[i:i+3]
        amino = genetic_code.get(codon, "")
        if amino == 'Stop' or not amino:
            return None
        peptide += amino
    return peptide

def solve_peptide_encoding(filename):
    genetic_code = {
        'AAA': 'K', 'AAC': 'N', 'AAG': 'K', 'AAU': 'N', 'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACU': 'T',
        'AGA': 'R', 'AGC': 'S', 'AGG': 'R', 'AGU': 'S', 'AUA': 'I', 'AUC': 'I', 'AUG': 'M', 'AUU': 'I',
        'CAA': 'Q', 'CAC': 'H', 'CAG': 'Q', 'CAU': 'H', 'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCU': 'P',
        'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGU': 'R', 'CUA': 'L', 'CUC': 'L', 'CUG': 'L', 'CUU': 'L',
        'GAA': 'E', 'GAC': 'D', 'GAG': 'E', 'GAU': 'D', 'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCU': 'A',
        'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGU': 'G', 'GUA': 'V', 'GUC': 'V', 'GUG': 'V', 'GUU': 'V',
        'UAA': 'Stop', 'UAC': 'Y', 'UAG': 'Stop', 'UAU': 'Y', 'UCA': 'S', 'UCC': 'S', 'UCG': 'S', 'UCU': 'S',
        'UGA': 'Stop', 'UGC': 'C', 'UGG': 'W', 'UGU': 'C', 'UUA': 'L', 'UUC': 'F', 'UUG': 'L', 'UUU': 'F'
    }

    with open(filename, 'r') as f:
        lines = f.read().splitlines()
        text = lines[0]
        peptide_target = lines[1]

    k = len(peptide_target) * 3
    results = []

    for i in range(len(text) - k + 1):
        substring = text[i:i+k]
        
        rna_forward = dna_to_rna(substring)
        if translate_rna(rna_forward, genetic_code) == peptide_target:
            results.append(substring)
            continue 
        rev_comp = reverse_complement(substring)
        rna_rev = dna_to_rna(rev_comp)
        if translate_rna(rna_rev, genetic_code) == peptide_target:
            results.append(substring)

    for res in results:
        print(res)

solve_peptide_encoding('dataset.txt')