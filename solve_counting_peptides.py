def solve_counting_peptides(filename):
    with open(filename, 'r') as f:
        m = int(f.read().strip())

    masses = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]
    
    dp = [0] * (m + 1)
    dp[0] = 1 
    
    for i in range(1, m + 1):
        for mass in masses:
            if i >= mass:
                dp[i] += dp[i - mass]
                
    print(dp[m])

solve_counting_peptides('dataset.txt')