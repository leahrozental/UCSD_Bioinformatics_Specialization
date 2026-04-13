def overlap_graph(patterns):
    adj_list = {}
    
    for i in range(len(patterns)):
        suffix = patterns[i][1:] 
        neighbors = []
        
        for j in range(len(patterns)):
            if i == j: 
                continue 
            
            prefix = patterns[j][:-1] 
            if suffix == prefix:
                neighbors.append(patterns[j])
        
        if neighbors:
            adj_list[patterns[i]] = neighbors
            
    return adj_list

with open('dataset.txt', 'r') as f:
    patterns = f.read().split()

graph = overlap_graph(patterns)

with open('answer.txt', 'w') as f:
    for node, edges in graph.items():
        line = f"{node}: {' '.join(edges)}\n"
        f.write(line)
        print(line.strip())