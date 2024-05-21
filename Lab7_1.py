from collections import Counter
from os.path import dirname
from re import findall

with open(dirname(__file__) + '\\Lab7_1.txt', 'r', encoding='utf-8') as file:
    text = file.read()

words = findall(r'\b\w+\b', text)
popularWord = Counter(words).most_common(1)[0]

print(f'Всего слов: {len(words)}')
print(f'Самое популярное слово «{popularWord[0]}» встречается {popularWord[1]} раз')