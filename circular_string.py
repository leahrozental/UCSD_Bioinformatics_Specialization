def solve_k_universal(filename):
    with open(filename, 'r') as f:
        line = f.read().strip()
        if not line: return
        k = int(line)

    adj = {}
    for i in range(2**(k-1)):
        prefix = bin(i)[2:].zfill(k-1)
        adj[prefix] = [prefix[1:] + '1', prefix[1:] + '0']

    start_node = '0' * (k-1)
    stack = [start_node]
    path = []

    while stack:
        u = stack[-1]
        if u in adj and adj[u]:
            v = adj[u].pop() 
            stack.append(v)
        else:
            path.append(stack.pop())
    

    cycle = path[::-1]
    result = ""
    for i in range(len(cycle) - 1):
        result += cycle[i][-1]
        
    print(result)

solve_k_universal('dataset.txt')