def solve():
    with open('dataset.txt', 'r') as f:
        n = int(f.read().strip())

    result = n * (n - 1)
    print(result)

solve()