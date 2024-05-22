# Импорт класса datetime из модуля datetime
from datetime import datetime
# Импорт функции dirname из модуля os.path
from os.path import dirname

# Объявление класса-декоратора
class Loging:
    def __init__(self, func):
        """
        Конструктор класса-декоратора.
        """
        self.func = func

    def __call__(self, *args, **kwargs):
        """
        Метод-обертка для декорируемой функции.
        """
        # Выполняем функции и сохраняем результат в переменную
        result = self.func(*args, **kwargs)
        # Формируем строку для журналирования в формате (текущее_время     наименование_функции(аргументы_функции)     результат_функции)
        logString = f'{datetime.now()}     {self.func.__name__}({str(', '.join(f'{element}' for element in args))}{', '.join(f'{key}={value}' for key, value in kwargs.items())})     {result}\n'
        # Открываем файл журнала в режиме добавления информации
        with open(dirname(__file__) + '\\Lab10_4.txt', 'a') as file:
            # Записываем сформированную строку в журнал
            file.write(logString)
        # Возвращаем результат функции
        return result

# Декорирование функции
@Loging
def adding(a, b):
    """
    Вычисление суммы чисел a и b.
    """
    return a + b

# Декорирование функции
@Loging
def subtracting(a, b):
    """
    Вычисление разности чисел a и b.
    """
    return a - b

# Запрос ввода числа a и сохранение его в переменную
a = int(input('Введите число a: '))
# Запрос ввода числа b и сохранение его в переменную
b = int(input('Введите число b: '))

# Вывод в терминал результатов работы программы
print(f'Сумма чисел {a} и {b} равна {adding(a, b)}, а разность равна {subtracting(a = a, b = b)}')