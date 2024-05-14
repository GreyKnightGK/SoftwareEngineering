from random import randint
from statistics import mean

def calcAvg(*args):
    print(f'Среднее арифметическое значений {args} равно {mean(args)}')

if __name__ == "__main__":
    calcAvg(*range(randint(0, 100)))