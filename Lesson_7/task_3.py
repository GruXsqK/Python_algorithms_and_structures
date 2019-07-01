# 3 Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше
# медианы, в другой — не больше медианы.
# Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно, используйте метод
# сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима).


import random


def median_search(array, ln_arr):

    if len(array) == 1:
        return array[0]

    pivot = random.choice(array)
    lows = []
    highs = []
    pivots = []

    for itm in array:
        if itm < pivot:
            lows += [itm]
        elif itm > pivot:
            highs += [itm]
        else:
            pivots += [itm]

    if ln_arr < len(lows):
        return median_search(lows, ln_arr)
    elif ln_arr < len(lows) + len(pivots):
        return pivots[0]
    else:
        return median_search(highs, ln_arr - len(lows) - len(pivots))


M = 500
MIN_NUMB = - 100
MAX_NUMB = 100

rnd_lst = [random.randint(MIN_NUMB, MAX_NUMB) for _ in range(2 * M + 1)]
print(rnd_lst)
print(f'Медиана в массиве = {median_search(rnd_lst, len(rnd_lst) / 2)}')
