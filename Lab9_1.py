# Объявление класса
class Tomato:
    # Словарь стадий созревания помидоров
    _states = {1: 'отсутствует', 2: 'цветение', 3: 'зеленый', 4: 'красный'}

    def __init__(self, index):
        """
        Конструктор класса.

        Аргументы:
            index - индекс
        """
        self._index = index     # Защищенный атрибут класса
        self._state = 1         # Защищенный атрибут класса

    def is_ripe(self):
        """
        Проверка, что томат созрел.
        """
        # Сравнивается текущее состояние томата с максимально возможным
        # Если значения совпадают - возвращается True, иначе False
        return self._state == max(self._states)
    
    def grow(self):
        """
        Перевод томата на следующую стадию созревания.
        """
        # Проверка, что томат еще не созрел
        if (not self.is_ripe()):
            # Перевод томата на следующую стадию созревания
            self._state += 1

# Объявление класса
class TomatoBush:
    def __init__(self, tomatoesCount):
        """
        Конструктор класса.

        Аргументы:
            tomatoesCount - количество томатов, которые будет содержать кус
        """
        # Генерация списка объектов Tomato
        self.tomatoes = [Tomato(i) for i in range(tomatoesCount)]

    def grow_all(self):
        """
        Перевод всех томатов на следующую стадию созревания.
        """
        # Начало цикла по списку tomatoes
        for tomato in self.tomatoes:
            # Перевод конкретного tomato на следующую стадию созревания
            tomato.grow()

    def all_are_ripe(self):
        """
        Проверка, что все томаты созрели.
        """
        # Возвращает True, если список tomatoes содержит элементы
        # и все Tomato в списке созрели, иначе возвращается False
        return len(self.tomatoes) > 0 and all(tomato.is_ripe() for tomato in self.tomatoes)
    
    def give_away_all(self):
        """
        Сбор урожая с куста.
        """
        # Очистка списка tomatoes
        self.tomatoes.clear()

# Объявление класса
class Gardener:
    def __init__(self, name, plant : TomatoBush):
        """
        Конструктор класса.

        Аргументы:
            name - имя садочника
            plant - куст, за которым садовник укаживает
        """
        self.name = name        # Публичный атрибут класса
        self._plant = plant     # Защищенный атрибут класса

    def work(self):
        """
        Выполнение садовником работы (позволяет растению становиться более зрелым).
        """
        # Перевод всех томатов на следующую стадию созревания
        self._plant.grow_all()

    def harvest(self):
        """
        Сбор урожая с куста, если все томаты поспели.
        """
        # Если все томаты поспели
        if (self._plant.all_are_ripe()):
            # Выполнить сбор урожая
            self._plant.give_away_all()
        # Иначе
        else:
            # Напечатать в терминале информацию о том, что собирать урожай пока рано
            print('Томаты еще не созрели')

    # Указание, что метод является статическим
    @staticmethod
    def knowledge_base():
        """
        Вывод справки в терминал.
        """
        # Выполнение команды вывода
        print('У Вас есть садовник и он знает, что делать для получения урожая')

# Вывод справки
Gardener.knowledge_base()

# Создание объекта TomatoBush с 15 объектами Tomato
tomatoBush = TomatoBush(15)
# Создание объекта Gardener и назначение его на ранее созданный объект TomatoBush
gardener = Gardener('Кирилл', tomatoBush)

# Выполнение работы садовником
gardener.work()
# Попытка сбора урожая
gardener.harvest()

# Запуск цикла
# Пока все томаты не созреют
while not tomatoBush.all_are_ripe():
    # Садовник работает
    gardener.work()
    # И об этом выводится информация в термиал
    print(f'{gardener.name} поработал')
# После этого
else:
    # Садовник собирает урожай
    gardener.harvest()
    # И факт сбора отображается в терминале
    print('Урожай успешной собран')