def solve():
    with open('dataset.txt', 'r') as f:
        data = f.read().split()
    
    if not data:
        return

    k = int(data[0])
    d = int(data[1])
    pairs = data[2:]

    
    first_parts = [p.split('|')[0] for p in pairs]
    prefix_string = first_parts[0]
    for i in range(1, len(first_parts)):
        prefix_string += first_parts[i][-1]

    second_parts = [p.split('|')[1] for p in pairs]
    suffix_string = second_parts[0]
    for i in range(1, len(second_parts)):
        suffix_string += second_parts[i][-1]

   
    overlap_start = k + d
    
    match = True
    for i in range(overlap_start, len(prefix_string)):
        if prefix_string[i] != suffix_string[i - overlap_start]:
            match = False
            break

    if match:
       
        print(prefix_string + suffix_string[-(overlap_start):])
    else:
        print("there is no string spelled by these gapped patterns")

solve()