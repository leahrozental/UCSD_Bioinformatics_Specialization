with open('dataset.txt', 'r') as f:
    k = int(f.readline().strip())  
    text = f.readline().strip()   

result = []
for i in range(len(text) - k + 1):
    fragment = text[i:i+k]
    result.append(fragment)

print(" ".join(result))
