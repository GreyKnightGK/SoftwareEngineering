from os.path import dirname
from re import findall

with open(dirname(__file__) + '\\input.txt', 'r') as file:
    text = file.readlines()

linesCount, wordsCount, lettersCount = 0, 0, 0
for line in text:
    line = line.strip()
    linesCount += 1
    wordsCount += len(findall(r'\b\w+\b', line))
    lettersCount += len(findall('[A-Za-z]', line))

print(f'Input file contains:\n{lettersCount} letters\n{wordsCount} words\n{linesCount} lines')