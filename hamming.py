def hamming_distance(p, q):
    distance = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            distance += 1
    return distance


try:
    with open("dataset2.txt", "r") as f:
        lines = f.read().splitlines()
        if len(lines) >= 2:
            str1 = lines[0].strip()
            str2 = lines[1].strip()
            
            print(hamming_distance(str1, str2))
        else:
            print("mistake: min 2 lines.")
except FileNotFoundError:
    print("not found.")