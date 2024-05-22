class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def move(self, distance):
        print(f'{self.name} пробежал {distance} метров')

class Bird(Animal):
    def __init__(self, name, age, beakShape):
        super().__init__(name, age)
        self.beakShape = beakShape

bird = Bird('Кеша', 1, 'зерноядный')

print(f'Переменная bird ссылается на объект класса {type(bird)}')