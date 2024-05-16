def removeElementByValue(tpl, value):
    if value in tpl:
        lst = list(tpl)
        lst.remove(value)
        return tuple(lst)
    else:
        return tpl

one = (1, 2, 3)
two = (1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2)
three = (2, 4, 6, 6, 4, 2)

print(removeElementByValue(one, 1))
print(removeElementByValue(two, 3))
print(removeElementByValue(three, 9))