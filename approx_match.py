def HammingDistance(p, q):
    # Компактный способ посчитать несовпадения
    return sum(1 for i in range(len(p)) if p[i] != q[i])

def ApproximatePatternMatching(Pattern, Text, d):
    positions = []
    k = len(Pattern)
    # Проходим по всему тексту «окном» длиной k
    for i in range(len(Text) - k + 1):
        substring = Text[i:i+k]
        if HammingDistance(Pattern, substring) <= d:
            positions.append(i)
    return positions

# Чтение данных из файла
try:
    with open("dataset.txt", "r") as f:
        lines = f.read().splitlines()
        pattern = lines[0].strip()
        text = lines[1].strip()
        d = int(lines[2].strip())
        
        # Получаем результат
        result = ApproximatePatternMatching(pattern, text, d)
        
        # Печатаем числа через пробел, как просит Stepik/Rosalind
        print(*(result))
except FileNotFoundError:
    print("Файл dataset.txt не найден! Положи его в папку с кодом.")