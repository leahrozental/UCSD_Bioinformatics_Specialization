from collections import defaultdict

def debruijn_from_kmers(patterns):
    adj = defaultdict(list)
    
    for kmer in patterns:
        prefix = kmer[:-1]
        suffix = kmer[1:] 
        adj[prefix].append(suffix)
    
    return adj

with open('dataset.txt', 'r') as f:
    patterns = f.read().split()

graph = debruijn_from_kmers(patterns)

with open('answer.txt', 'w') as f:
    for node in sorted(graph.keys()):
        neighbors = " ".join(sorted(graph[node]))
        line = f"{node}: {neighbors}\n"
        f.write(line)
        print(line.strip())