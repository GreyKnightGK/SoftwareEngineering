value = input('Введите последовательность чисел, разделенных пробелом: ')
numberList = [x for x in value.split() if x.isnumeric()]
print(numberList)
print(tuple(numberList))