from os.path import dirname

def fib(n):
    a, b = 1, 1
    for x in range(n):
        a, b = b, a + b
        yield b

fibonacci = fib(200)
fileName = 'fib.txt'

with open(dirname(__file__) + f'\\{fileName}', 'a') as file:
    for i in fibonacci:
        file.write(f'{i}\n')
    else:
        print(f'Вычисление последовательности чисел Фибоначи завершено, результат сохранен в файл {fileName}.')