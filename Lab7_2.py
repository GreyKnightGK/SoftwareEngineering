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