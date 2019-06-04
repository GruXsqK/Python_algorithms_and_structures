# Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random


MIN_NUMB = -100
MAX_NUMB = 100
COUNT_COLUMN = 10
COUNT_LINE = 10

matrix = [[random.randint(MIN_NUMB, MAX_NUMB) for _ in range(COUNT_COLUMN)] for _ in range(COUNT_LINE)]

# for line in matrix:
#     print(line)

min_elem_lst = []
j = 0

while j < COUNT_COLUMN:
    i = 1
    min_elem = matrix[0][j]
    while i < COUNT_LINE:
        if matrix[i][j] < min_elem:
            min_elem = matrix[i][j]
        i += 1
    min_elem_lst.append(min_elem)
    j += 1

max_elm = min_elem_lst[0]

for elm in min_elem_lst:
    if elm > max_elm:
        max_elm = elm

print(f'Максимальный элемент среди минимальных элементов столбцов матрицы = {max_elm}')
