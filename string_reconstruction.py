def solve_string_reconstruction(filename):
    with open(filename, 'r') as f:
        lines = f.read().splitlines()
        if not lines: return
        k = int(lines[0])
        patterns = []
        for line in lines[1:]:
            patterns.extend(line.split())

    adj = {}
    in_degree = {}
    out_degree = {}
    
    for p in patterns:
        prefix = p[:-1]
        suffix = p[1:]
        if prefix not in adj:
            adj[prefix] = []
        adj[prefix].append(suffix)
        
        out_degree[prefix] = out_degree.get(prefix, 0) + 1
        in_degree[suffix] = in_degree.get(suffix, 0) + 1

    start_node = patterns[0][:-1] 
    nodes = set(adj.keys()) | set(in_degree.keys())
    for node in nodes:
        if out_degree.get(node, 0) > in_degree.get(node, 0):
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
    
    euler_path = path[::-1]

    text = euler_path[0]
    for i in range(1, len(euler_path)):
        text += euler_path[i][-1]
    
    print(text)


solve_string_reconstruction('dataset.txt')