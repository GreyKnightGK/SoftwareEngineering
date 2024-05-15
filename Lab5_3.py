from math import sqrt

def calculateTriangleArea(a, b, c):
    # Полупериметр треугольника
    p = 0.5 * (a + b + c)
    # Площадь треугольника
    S = sqrt(p * (p - a) * (p - b) * (p - c))
    return S

one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]

print(f'Площадь max: {calculateTriangleArea(max(one), max(two), max(three))}')
print(f'Площадь min: {calculateTriangleArea(min(one), min(two), min(three))}')