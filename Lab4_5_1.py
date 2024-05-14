# Lab4_5_1.py
from math import sqrt

def calculateTriangleArea(a, b, c):
    # Полупериметр треугольника
    p = 0.5 * (a + b + c)
    # Площадь треугольника
    S = sqrt(p * (p - a) * (p - b) * (p - c))
    return S