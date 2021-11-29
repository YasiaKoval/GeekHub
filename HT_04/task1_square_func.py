# 1. Написати функцію < square > , яка прийматиме один аргумент - сторону квадрата, і вертатиме 3 значення (кортеж):
# периметр квадрата, площа квадрата та його діагональ.
import math


def square(sqside):
    persq = 4*sqside
    ssq = sqside**2
    diagsq = sqside*(math.sqrt(2))
    print((persq, ssq, diagsq))


square(float(input('Введіть сторону квадрата: ')))
