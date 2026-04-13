def find_minimum_skew(filename):
    try:
        with open(filename, 'r') as f:
            genome = f.read().strip()
    except FileNotFoundError:
        print("not found")
        return

    skew = 0
    min_skew = 0
    positions = [0]
    
    for i, base in enumerate(genome):
        if base == 'G':
            skew += 1
        elif base == 'C':
            skew -= 1
        
        current_pos = i + 1
        
        if skew < min_skew:
            min_skew = skew
            positions = [current_pos]
        elif skew == min_skew:
            positions.append(current_pos)
            
    print("answer:")
    print(*(positions))

find_minimum_skew('genome.txt')