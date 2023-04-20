# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

import random

n = int(input("Введите количество элементов массива: "))

list = []

for i in range(n):
    list.append(random.randint(-10,10))

x = int(input("Введите x: "))
result = list[0]
eps = x

for i in list:
    if abs(i - x) < eps:
        eps = abs(i - x)
        result = i

print(list)

print(result)
