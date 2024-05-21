# Тема 7. Работа с файлами (ввод, вывод)
Отчет по Теме #7 выполнил:
- Шишканов Сергей Сергеевич
- ИНО ОЗБ ПОАС-22-2

| Задание | Сам_раб |
| ------ | ------ |
| Задание 1 | + |
| Задание 2 | + |
| Задание 3 | + |
| Задание 4 | + |
| Задание 5 | + |

Работу проверили:
- к.э.н., доцент Панов М.А.

## Самостоятельная работа №1
### Задание
Найдите в интернете любую статью (объем статьи не менее 200 слов), скопируйте ее содержимое в файл и напишите программу,
которая считает количество слов в текстовом файле и определит самое часто встречающееся слово.\
Результатом выполнения задачи будет: скриншот файла со статьей, листинг кода, и вывод в консоль, в котором будет указана вся необходимая информация.

### Код
```python
from collections import Counter
from os.path import dirname
from re import findall

with open(dirname(__file__) + '\\Lab7_1.txt', 'r', encoding='utf-8') as file:
    text = file.read()

words = findall(r'\b\w+\b', text)
popularWord = Counter(words).most_common(1)[0]

print(f'Всего слов: {len(words)}')
print(f'Самое популярное слово «{popularWord[0]}» встречается {popularWord[1]} раз')
```

### Результат
![](https://github.com/GreyKnightGK/SoftwareEngineering/blob/Тема_7/pic/Lab7_1.png)

## Самостоятельная работа №2
### Задание
У вас появилась потребность в ведении книги расходов, посмотрев все существующие варианты вы пришли к выводу что вас ничего не устраивает и нужно все делать самому.
Напишите программу для учета расходов. Программа должна позволять вводить информацию о расходах, сохранять ее в файл и выводить существующие данные в консоль.
Ввод информации происходит через консоль.\
Результатом выполнения задачи будет: скриншот файла с учетом расходов, листинг кода, и вывод в консоль, с демонстрацией работоспособности программы.

### Код
```python
from os.path import dirname

fileName = dirname(__file__) + '\\Lab7_2.txt'

def addExpenses(name, sum):
        with open(fileName, 'a', encoding='utf-8') as file:
            file.write(f'{name}: {sum} ₽\n')
        print('Расходы успешно внесены.')

def readExpenses():
    try:
        with open(fileName, 'r', encoding='utf-8') as file:
            print(file.read())
    except FileNotFoundError:
         print('Вы еще не вносили расходы.')

action = input('Вы хотите добавить (+) или просмотреть (=) расходы? ')
if (action == '+'):
    expensesName = input('На что потратили? ')
    expensesSum = input('Как много? ')
    addExpenses(expensesName, expensesSum)
elif (action == '='):
    readExpenses()
else:
    print('Неизвестное действие')
```

### Результат
![](https://github.com/GreyKnightGK/SoftwareEngineering/blob/Тема_7/pic/Lab7_2.png)

## Самостоятельная работа №3
### Задание
Имеется файл input.txt с текстом на латинице. Напишите программу, которая выводит следующую статистику по тексту: количество букв
латинского алфавита; число слов; число строк.

Текст в файле:\
Beautiful is better than ugly.\
Explicit is better than implicit.\
Simple is better than complex.\
Complex is better than complicated.

Ожидаемый результат:\
Input file contains:\
108 letters\
20 words\
4 lines

### Код
```python
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
```

### Результат
![](https://github.com/GreyKnightGK/SoftwareEngineering/blob/Тема_7/pic/Lab7_3.png)

## Самостоятельная работа №4
### Задание
Напишите программу, которая получает на вход предложение, выводит его в терминал, заменяя все запрещенные слова
звездочками \* (количество звездочек равно количеству букв в слове).
Запрещенные слова, разделенные символом пробела, хранятся в текстовом файле input.txt.
Все слова в этом файле записаны в нижнем регистре. Программа должна заменить запрещенные слова, где бы они ни встречались,
даже в середине другого слова. Замена производится независимо от регистра: если файл input.txt содержит запрещенное слово exam, то слова exam,
Exam, ExaM, EXAM и exAm должны быть заменены на \*\*\*\*.

Запрещенные слова:\
hello email python the exam wor is

Предложение для проверки:\
Hello, world! Python IS the programming language of thE future. My EMAIL is....\
PYTHON is awesome!!!!

Ожидаемый результат:\
\*\*\*\*\*, \*\*\*ld! \*\*\*\*\*\* \*\* \*\*\* programming language of \*\*\* future. My \*\*\*\*\* \*\*....\
\*\*\*\*\*\* \*\* awesome!!!!

### Код
```python
from os.path import dirname
import re

with open(dirname(__file__) + '\\input.txt', 'r') as file:
    forbiddenWords = file.read().split(' ')

text = 'Hello, world! Python IS the programming language of thE future. My EMAIL is....\nPYTHON is awesome!!!!'
for word in forbiddenWords:
    text = re.sub(word, '*' * len(word), text, flags=re.IGNORECASE)

print(text)
```

### Результат
![](https://github.com/GreyKnightGK/SoftwareEngineering/blob/Тема_7/pic/Lab7_4.png)

## Самостоятельная работа №5
### Задание
Самостоятельно придумайте и решите задачу, которая будет взаимодействовать с текстовым файлом.

Дано X файлов, необходимо объединить их содержимое в один файл. В объединенном файле содержимое каждого добавленного файла должно начинаться с новой строки.\
Вывести в терминал содержимое объединяемых файлов (минимум 3 файла) и объединенного файла.

### Код
```python
from os.path import dirname

dirName = dirname(__file__) + '\\'
inputFiles = ('file1.txt', 'file2.txt', 'file3.txt')

with open(dirName + 'output.txt', 'a+') as outputFile:
    for file in inputFiles:
        with open(dirName + file, 'r') as inputFile:
            text = inputFile.read()
        outputFile.write(text + '\n')
        print(f'Текст файла {file}:\n{text}\n')
    outputFile.seek(0)
    print(f'Текст объединенного файла:\n{outputFile.read()}')
```

### Результат
![](https://github.com/GreyKnightGK/SoftwareEngineering/blob/Тема_7/pic/Lab7_5.png)