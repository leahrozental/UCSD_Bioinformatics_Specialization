def solve_eulerian_path(filename):
    adj = {}
    in_degree = {}
    out_degree = {}

    with open(filename, 'r') as f:
        for line in f:
            if ':' not in line: continue
            u, neighbors = line.split(':')
            u = int(u)
            neighbors = [int(n) for n in neighbors.split()]
            adj[u] = neighbors
            
            out_degree[u] = out_degree.get(u, 0) + len(neighbors)
            for v in neighbors:
                in_degree[v] = in_degree.get(v, 0) + 1

    start_node = next(iter(adj))
    all_nodes = set(adj.keys()) | set(in_degree.keys())
    
    for node in all_nodes:
        out_d = out_degree.get(node, 0)
        in_d = in_degree.get(node, 0)
        if out_d > in_d:
            start_node = node
            break

    stack = [start_node]
    path = []

    while stack:
        u = stack[-1]
        if u in adj and adj[u]:
            v = adj[u].pop()
            stack.append(v)
        else:
            path.append(stack.pop())

    print(*(path[::-1]))

solve_eulerian_path('dataset.txt')