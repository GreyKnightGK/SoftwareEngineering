def filterCards (cards, value):
    return [x for x in cards if not x.isnumeric() or int(x) >= value]

cardGame = input('Колода для какой игры (покер, дурак, преферанс, тысяча) Вам требуется? ').lower()

cardSuits = ('♠', '♥', '♦', '♣')
cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'В', 'Д', 'К', 'Т']

if (cardGame == 'покер'):
    pass
elif (cardGame == 'дурак'):
    cards = filterCards(cards, 6)
elif (cardGame == 'преферанс'):
    cards = filterCards(cards, 7)
elif (cardGame == 'тысяча'):
    cards = filterCards(cards, 9)
else:
    print('Неизвестная игра')
    exit()

print(f'Колода для игры в {cardGame}: {tuple((card+suit) for suit in cardSuits for card in cards)}')