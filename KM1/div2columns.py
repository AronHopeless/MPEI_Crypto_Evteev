from collections import Counter

text = ""

for i in range(0, len(text), 4):
    chunk = text[i:i+4]          
    print(" ".join(chunk))       
    
print('\n\n____________________\n\n')

# счётчики для каждого из 4 столбцов
counters = [Counter(), Counter(), Counter(), Counter()]

# распределяем символы по столбцам
for i in range(0, len(text) - 1, 4):
    for j in range(4):
        if i + j < len(text):
            counters[j][text[i + j]] += 1

# выводим результаты
for idx, counter in enumerate(counters, start=1):
    print(f"\nСтолбец {idx}:")
    for symbol, count in counter.most_common():
        print(f"{symbol}: {count}")


