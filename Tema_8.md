# Тема 8. Введение в ООП
Отчет по Теме #8 выполнил:
- Шишканов Сергей Сергеевич
- ИНО ОЗБ ПОАС-22-2

| Задание | Сам_раб |
| ------ | ------ |
| Задание 1 | + |
| Задание 2 | + |
| Задание 3 | + |
| Задание 4 | + |
| Задание 5 | + |

Работу проверили:
- к.э.н., доцент Панов М.А.

## Самостоятельная работа №1
### Задание
Самостоятельно создайте класс и его объект. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях.
Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

### Код
```python
class Animal:
    def __init__(self):
        pass

animal = Animal()

print(f'Переменная animal ссылается на объект класса {type(animal)}')
```

### Результат
![](https://github.com/GreyKnightGK/SoftwareEngineering/blob/Тема_8/pic/Lab8_1.png)

## Самостоятельная работа №2
### Задание
Самостоятельно создайте атрибуты и методы для ранее созданного класса. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях.
Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

### Код
```python
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def move(self, distance):
        print(f'{self.name} пробежал {distance} метров')

animal = Animal('Шарик', 3)
animal.move(5)
```

### Результат
![](https://github.com/GreyKnightGK/SoftwareEngineering/blob/Тема_8/pic/Lab8_2.png)

## Самостоятельная работа №3
### Задание
Самостоятельно реализуйте наследование, продолжая работать с ранее созданным классом. Оно должно отличаться, от того, что указано в теоретическом материале (методичке) и лабораторных
заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

### Код
```python
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
```

### Результат
![](https://github.com/GreyKnightGK/SoftwareEngineering/blob/Тема_8/pic/Lab8_3.png)

## Самостоятельная работа №4
### Задание
Самостоятельно реализуйте инкапсуляцию, продолжая работать с ранее созданным классом. Она должна отличаться, от того, что указана в теоретическом материале (методичке) и лабораторных
заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

### Код
```python
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
bird.getInfo()
```

### Результат
![](https://github.com/GreyKnightGK/SoftwareEngineering/blob/Тема_8/pic/Lab8_4.png)

## Самостоятельная работа №5
### Задание
Самостоятельно реализуйте полиморфизм. Он должен отличаться, от того, что указан в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет
листинг кода и получившийся вывод консоли.

### Код
```python
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
```

### Результат
![](https://github.com/GreyKnightGK/SoftwareEngineering/blob/Тема_8/pic/Lab8_5.png)