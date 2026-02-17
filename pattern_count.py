def hamming_distance(p, q):
    return sum(1 for a, b in zip(p, q) if a != b)

def approximate_pattern_count(pattern, text, d):
    count = 0
    k = len(pattern)
    for i in range(len(text) - k + 1):
        window = text[i:i + k]
        if hamming_distance(pattern, window) <= d:
            count += 1
    return count

try:
    with open("dataset.txt", "r") as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]
        
        if len(lines) >= 3:
            pattern = lines[0]
            text = lines[1]
            d = int(lines[2])
            
            result = approximate_pattern_count(pattern, text, d)
            print(f"result (Count_d): {result}")
        else:
            print("error: 3 lines")
            
except FileNotFoundError:
    print("FileNotFoundError")
except ValueError:
    print("error: without d")