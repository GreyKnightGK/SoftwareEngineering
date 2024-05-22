import re

class WrongSymbolsException(Exception):
    def __init__ (self, message):
        self.message = message

def cyrillicString(string):
    if (not re.match('^[А-Яа-яЁё]+$', string)):
        raise WrongSymbolsException('Строка должна содержать только кириллические символы.')
    return f'Строка содержит {len(string)} кириллических символов'

def numberString(string):
    if (not re.match('^[0-9]+$', string)):
        raise WrongSymbolsException('Строка должна содержать только цифры.')
    return f'Строка содержит {len(string)} цифр'

cyrillicStr = input('Введите текст на кириллице: ')
try:
    print(cyrillicString(cyrillicStr))
except WrongSymbolsException as e:
    print(e.message)

numberStr = input('Введите цифры: ')
try:
    print(numberString(numberStr))
except WrongSymbolsException as e:
    print(e.message)