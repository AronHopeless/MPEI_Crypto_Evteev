from collections import Counter

text = ""

for i in range(0, len(text) - 1, 4):
    print(text[i]+" "+text[i+1]+" "+text[i+2]+" "+text[i+3])
    
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

