def solve_eulerian_cycle(filename):
    adj = {}
    
    with open(filename, 'r') as f:
        for line in f:
            if ':' not in line: continue
            node, neighbors = line.split(':')
            adj[int(node)] = [int(n) for n in neighbors.split()]

    stack = [6]
    path = []

    while stack:
        u = stack[-1]
        if u in adj and adj[u]:
            v = adj[u].pop()
            stack.append(v)
        else:
            path.append(stack.pop())

    print(*(path[::-1]))

solve_eulerian_cycle('dataset.txt')