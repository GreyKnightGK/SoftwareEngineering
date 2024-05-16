from random import randint
from collections import Counter

def getRandomNumericString():
    string = str()
    for value in range(25):
        string += str(randint(0, 9))
    return string

def getNumericDict(str):
    return dict(sorted(Counter(str).most_common(3)))

string = getRandomNumericString()

print(f'Случайная строка: {string}')
print(f'Чаще всего в строке встречаются следущие числа: {getNumericDict(string)}')