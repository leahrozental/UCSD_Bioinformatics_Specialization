def solve_paired_reconstruction(filename):
    with open(filename, 'r') as f:
        lines = f.read().splitlines()
        first_line = lines[0].split()
        k, d = int(first_line[0]), int(first_line[1])
        pairs = []
        for line in lines[1:]:
            pairs.extend(line.split())

    adj = {}
    in_degree = {}
    out_degree = {}

    for pair in pairs:
        read1, read2 = pair.split('|')
        u = (read1[:-1], read2[:-1]) 
        v = (read1[1:], read2[1:])   
        
        if u not in adj: adj[u] = []
        adj[u].append(v)
        
        out_degree[u] = out_degree.get(u, 0) + 1
        in_degree[v] = in_degree.get(v, 0) + 1

    start_node = None
    all_nodes = set(adj.keys()) | set(in_degree.keys())
    for node in all_nodes:
        if out_degree.get(node, 0) > in_degree.get(node, 0):
            start_node = node
            break
    if not start_node: start_node = pairs[0].split('|')[0][:-1], pairs[0].split('|')[1][:-1]

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

    prefix_string = euler_path[0][0]
    suffix_string = euler_path[0][1]
    
    for i in range(1, len(euler_path)):
        prefix_string += euler_path[i][0][-1]
        suffix_string += euler_path[i][1][-1]


    overlap_len = len(prefix_string) - (k + d)
    result = prefix_string + suffix_string[-(k + d):]
    
    print(result)

solve_paired_reconstruction('dataset.txt')