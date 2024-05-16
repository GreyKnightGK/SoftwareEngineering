def search(tpl, value):
    if (value in tpl):
        firstIndex = tpl.index(value)
        if (value in tpl[firstIndex + 1:]):
            secondIndex = tpl.index(value, firstIndex+1)
            return tpl[firstIndex:secondIndex + 1]
        else:
            return tpl[firstIndex:]
    else:
        return ()

one = (1, 2, 3)
two = (1, 8, 3, 4, 8, 8, 9, 2)
three = (1, 2, 8, 5, 1, 2, 9)

print(search(one, 8))
print(search(two, 8))
print(search(three, 8))