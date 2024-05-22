class Animal:
    def __init__(self, name, age):
        self._name = name
        self.__age = age

    def getInfo(self):
        print(f'{self._name} {'недавно родился' if self.__age <= 1 else 'с нами уже ' + str(self.__age) + (' года' if self.__age < 5 else ' лет')}')
    
    def move(self, distance):
        print(f'{self._name} пробежал {distance} метров')

class Bird(Animal):
    def __init__(self, name, age, beakShape):
        super().__init__(name, age)
        self.beakShape = beakShape

    def move(self, distance):
        print(f'{self._name} пролетел {distance} метров')

animal = Animal('Шарик', 3)
animal.move(5)

bird = Bird('Кеша', 1, 'зерноядный')
bird.move(10)