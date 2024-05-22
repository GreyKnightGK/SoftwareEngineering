def addTwo(number):
        return 2 + int(number)

userInput = input('Введите целое число: ')
try:
     print(f'После добавления 2 получилось {addTwo(userInput)}')
except ValueError:
     print('Неподходящий тип данных. Ожидалось целое число.')