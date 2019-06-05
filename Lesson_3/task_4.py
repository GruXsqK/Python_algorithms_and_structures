# Определить, какое число в массиве встречается чаще всего.

import random


MIN_NUMB = 0
MAX_NUMB = 100
COUNT_NUMB = 500

num_tpl = tuple(random.randint(MIN_NUMB, MAX_NUMB) for _ in range(COUNT_NUMB))
num_count = {}

for elm in num_tpl:
    if elm in num_count.keys():
        num_count[elm] += 1
    else:
        num_count[elm] = 1

max_count = 0
num_max_count = 0

for key, elm in num_count.items():
    if num_count[key] > max_count:
        max_count = num_count[key]
        num_max_count = key

print(f'Число {num_max_count} встречается чаще всего ({max_count} раз)')
