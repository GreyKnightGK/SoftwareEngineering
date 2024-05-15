from collections import Counter

def createSet(list):
    result = set()
    for value in Counter(list).items():
        i = 1
        while i <= value[1]:
            result.add(value[0]) if (i == 1) else result.add(str(value[0]) * i)
            i += 1
    return result

list_1 = [1, 1, 3, 3, 1]
list_2 = [5, 5, 5, 5, 5, 5, 5]
list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]

print(createSet(list_1))
print(createSet(list_2))
print(createSet(list_3))