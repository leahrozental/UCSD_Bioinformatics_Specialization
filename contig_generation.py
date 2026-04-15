def solve_contig_generation(filename):
    with open(filename, 'r') as f:
        patterns = f.read().split()

    adj = {}
    in_degree = {}
    out_degree = {}
    
    for p in patterns:
        u, v = p[:-1], p[1:]
        if u not in adj: adj[u] = []
        adj[u].append(v)
        out_degree[u] = out_degree.get(u, 0) + 1
        in_degree[v] = in_degree.get(v, 0) + 1

    nodes = set(adj.keys()) | set(in_degree.keys())
    contigs = []

    for start_node in nodes:
        if not (in_degree.get(start_node, 0) == 1 and out_degree.get(start_node, 0) == 1):
            if out_degree.get(start_node, 0) > 0:
                for next_node in adj[start_node]:
                    contig = start_node + next_node[-1]
                    curr = next_node
                    while in_degree.get(curr, 0) == 1 and out_degree.get(curr, 0) == 1:
                        curr = adj[curr][0]
                        contig += curr[-1]
                    contigs.append(contig)

   
    print(*(sorted(contigs)))

solve_contig_generation('dataset.txt')
