from random import randint

def diceRoll():
    result = randint(1, 6)
    print(f'На кубике выпало {result}')

    if result in (5, 6):
        print('Вы победили')
    elif result in (1, 2):
        print('Вы проиграли')
    else:
        diceRoll()

if __name__ == '__main__':
    diceRoll()