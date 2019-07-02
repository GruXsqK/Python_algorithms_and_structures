# 1 Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на
# промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Примечания:
# ● алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
# ● постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
# Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.


from random import randint


def bubble_sort(array, flag=True):
    n = 1
    while n < len(array):
        change = 0
        for i in range(len(array) - n):
            if not flag:
                if array[i] < array[i + 1]:
                    array[i], array[i + 1] = array[i + 1], array[i]
                    change += 1
            else:
                if array[i] > array[i + 1]:
                    array[i], array[i + 1] = array[i + 1], array[i]
                    change += 1
        n += 1
        if change == 0:
            break
    return array


SIZE = 1000
MIN_NUMB = - 100        # включительно
MAX_NUMB = 100          # исключительно

rnd_lst = [randint(MIN_NUMB, MAX_NUMB - 1) for _ in range(SIZE)]
print(rnd_lst)
print(bubble_sort(rnd_lst, flag=False))
