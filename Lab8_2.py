class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def move(self, distance):
        print(f'{self.name} пробежал {distance} метров')

animal = Animal('Шарик', 3)
animal.move(5)