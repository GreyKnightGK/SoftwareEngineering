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

bird = Bird('Кеша', 1, 'зерноядный')
bird.move(5)