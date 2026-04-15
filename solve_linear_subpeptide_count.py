def solve_linear_subpeptide_count(filename):
    with open(filename, 'r') as f:
        line = f.read().strip()
        if not line: return
        n = int(line)

    result = (n * (n + 1) // 2) + 1
    print(result)

solve_linear_subpeptide_count('dataset.txt')