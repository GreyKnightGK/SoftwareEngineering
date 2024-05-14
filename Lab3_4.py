text = input('Введите предложение: ')
lowerText = text.lower()

print(f'Длина предложения: {len(text)} символов.')
print(f'Предложение в нижнем регистре: {lowerText}')
print(f'Количество латинских гласных (a, e, i, o, u) в предложении: {sum(1 for char in lowerText if char in 'aeiou')}')
print(f'Предложение после замены "ugly" на "beauty": {text.replace('ugly', 'beauty')}')
print(f'Предложение {'' if lowerText.startswith("the") else 'не '}начинается на "The" и {'' if lowerText.endswith("end") else 'не '}заканчивается на "end".')