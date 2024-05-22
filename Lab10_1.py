from time import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        startTime = time()
        result = func(*args, **kwargs)
        endTime = time()
        print(f'\nВремя выполнения {func.__name__}: {endTime - startTime} секунд')
        return result
    return wrapper

@measure_time
def fibonacci():
    fib1 = fib2 = 1

    for i in range(2, 200):
        fib1, fib2 = fib2, fib1 + fib2
        print(fib2, end='')

if __name__ == '__main__':
    fibonacci()