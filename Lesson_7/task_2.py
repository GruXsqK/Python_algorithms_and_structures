# 2 Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на
# промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

from random import random


def merge_sort(array):
    if len(array) <= 1:
        return array

    left = merge_sort(array[:len(array)//2])
    right = merge_sort(array[len(array)//2:])

    i = j = k = 0

    while i < len(left) or j < len(right):
        if not i < len(left):
            array[k] = right[j]
            j += 1
            k += 1
        elif not j < len(right):
            array[k] = left[i]
            i += 1
            k += 1
        elif left[i] < right[j]:
            array[k] = left[i]
            i += 1
            k += 1
        else:
            array[k] = right[j]
            j += 1
            k += 1

    return array


SIZE = 500
MAX_NUMB = 50       # исключительно

rnd_lst = [random() * MAX_NUMB for _ in range(SIZE)]
print(rnd_lst)
print(merge_sort(rnd_lst))
