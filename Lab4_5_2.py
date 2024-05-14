# Lab4_5_2.py
from Lab4_5_1 import calculateTriangleArea

triangleSide = []
for side in ('a', 'b', 'c'):
    triangleSide.append(int(input(f'Введите длину стороны {side}: ')))

print(f'Площадь треугольника равна {calculateTriangleArea(*triangleSide)}')