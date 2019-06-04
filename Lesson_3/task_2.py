# Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со
# значениями 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.

import random


MIN_NUMB = 1
MAX_NUMB = 50
COUNT_NUMB = 100


lst_a = [random.randint(MIN_NUMB, MAX_NUMB) for _ in range(COUNT_NUMB)]
lst_b = []
i = 0

while i < len(lst_a):
    if lst_a[i] != 0 and lst_a[i] % 2 == 0:
        lst_b.append(i)
    i += 1

print(f'Список чисел: {lst_a}')
print(f'Индексы четных чисел: {lst_b}')
