# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random


MIN_NUMB = 0
MAX_NUMB = 100
COUNT_NUMB = 500

num_tpl = tuple(random.randint(MIN_NUMB, MAX_NUMB) for _ in range(COUNT_NUMB))
max_num = num_tpl[0]
min_num = num_tpl[0]
max_num_idx = 0
min_num_idx = 0

for idx, elm in enumerate(num_tpl):
    if max_num < elm:
        max_num = elm
        max_num_idx = idx
    if min_num > elm:
        min_num = elm
        min_num_idx = idx

if min_num_idx > max_num_idx:
    idx_1, idx_2 = max_num_idx, min_num_idx
else:
    idx_1, idx_2 = min_num_idx, max_num_idx

sum_num = 0

while idx_1 + 1 < idx_2:
    sum_num += num_tpl[idx_1+1]
    idx_1 += 1

print(f'Одномерный массив: {num_tpl}')
print(f'Сумма чисел в массиве между максимальным и минимальным: {sum_num}')
