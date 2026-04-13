from collections import defaultdict

def debruijn_graph(k, text):
    adj = defaultdict(list)
    
    for i in range(len(text) - k + 1):
        kmer = text[i:i+k]
        prefix = kmer[:-1] 
        suffix = kmer[1:] 
        adj[prefix].append(suffix)
    
    return adj

with open('dataset.txt', 'r') as f:
    lines = f.read().splitlines()
    k = int(lines[0])
    text = lines[1]

graph = debruijn_graph(k, text)

with open('answer.txt', 'w') as f:
    for node in sorted(graph.keys()):
        neighbors = " ".join(sorted(graph[node]))
        line = f"{node}: {neighbors}\n"
        f.write(line)
        print(line.strip())