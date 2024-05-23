def fib(n):
    a, b = 1, 1
    for x in range(n):
        a, b = b, a + b
        yield b

fibonacci = fib(200)

for i in fibonacci:
    pass
else:
    print(f'Вычисленное число Фибоначи: {i}')