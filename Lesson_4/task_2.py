# Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать
# на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
#
# Первый — с помощью алгоритма «Решето Эратосфена».
# Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков.
# Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.
#
# Второй — без использования «Решета Эратосфена».


import cProfile


def sieve(n):

    size = int(n ** 1.5 + 2)
    sie = [i for i in range(size)]
    sie[1] = 0

    for i in range(2, size):
        if sie[i] != 0:
            j = i + i

            while j < size:
                sie[j] = 0
                j += i

    res = [i for i in sie if i != 0]
    return res[n - 1]


# cProfile.run('sieve(2000)')

# python -m timeit -n 100 -s "import task_2" "task_2.sieve(500)"
# 100 loops, best of 5: 3.84 msec per loop
# 1    0.003    0.003    0.004    0.004 task_2.py:14(sieve)
# 1    0.000    0.000    0.000    0.000 task_2.py:17(<listcomp>)
# 1    0.000    0.000    0.000    0.000 task_2.py:28(<listcomp>)

# python -m timeit -n 100 -s "import task_2" "task_2.sieve(1000)"
# 100 loops, best of 5: 11.4 msec per loop
# 1    0.011    0.011    0.014    0.014 task_2.py:14(sieve)
# 1    0.002    0.002    0.002    0.002 task_2.py:17(<listcomp>)
# 1    0.001    0.001    0.001    0.001 task_2.py:28(<listcomp>)

# python -m timeit -n 100 -s "import task_2" "task_2.sieve(2000)"
# 100 loops, best of 5: 34.8 msec per loop
# 1    0.032    0.032    0.039    0.039 task_2.py:14(sieve)
# 1    0.005    0.005    0.005    0.005 task_2.py:17(<listcomp>)
# 1    0.003    0.003    0.003    0.003 task_2.py:28(<listcomp>)


def prime_number(n):

    if n == 1:
        return 2

    res = [2]
    numb_list = [2]
    numb = 3

    while len(res) != n:
        flag = True

        for itm in numb_list:
            if numb % itm == 0:
                flag = False
                break

        if flag:
            res.append(numb)

        numb_list.append(numb)
        numb += 1

    return res[n - 1]


# cProfile.run('prime_number(2000)')

# python -m timeit -n 100 -s "import task_2" "task_2.prime_number(500)"
# 100 loops, best of 5: 44.1 msec per loop
#     1   0.069    0.069    0.069    0.069   task_2.py: 59(prime_number)
#     1   0.000    0.000    0.069    0.069   {built - in method builtins.exec}
#  3570   0.000    0.000    0.000    0.000   {built - in method builtins.len}
#  4068   0.000    0.000    0.000    0.000   {method 'append' of 'list' objects}

# python -m timeit -n 100 -s "import task_2" "task_2.prime_number(1000)"
# 100 loops, best of 5: 203 msec per loop
#     1   0.239    0.239    0.240    0.240    task_2.py: 59(prime_number)
#     1   0.000    0.000    0.240    0.240    {built - in method builtins.exec}
#  7918   0.001    0.000    0.001    0.000    {built - in method builtins.len}
#  8916   0.001    0.000    0.001    0.000    {method 'append' of 'list' objects}

# python -m timeit -n 100 -s "import task_2" "task_2.prime_number(2000)"
# 100 loops, best of 5: 902 msec per loop
#      1    1.008    1.008    1.011    1.011   task_2.py: 59(prime_number)
#      1    0.000    0.000    1.011    1.011   {built - in method builtins.exec}
#  17388    0.001    0.000    0.001    0.000   {built - in method builtins.len}
#  19386    0.001    0.000    0.001    0.000   {method 'append' of 'list' objects}


# Поиск натурального числа по алгоритму решета Эратосфена работает быстрее, и имеет сложность близкую к линейной
# O(n) по сравнению с алгоритмом prime_number(n), где используется перебор всех элементов, и который имеет сложность
# O(n^2). Подобная скорость работы алгоритма решета достигается правильным подбором размера массива натуральных чисел.
# Размер массива (size = int(n ** 1.5 + 2)) растет немного быстрее, чем функция распределения простых чисед.
# При размере size = n ** 2 сложность алгоритма решета будет O(n^2) и скорость работы станет даже ниже, чем у
# prime_number(n).

# python -m timeit -n 100 -s "import task_2" "task_2.sieve(500)"
# 100 loops, best of 5: 106 msec per loop (при size = n ** 2)

# python -m timeit -n 100 -s "import task_2" "task_2.sieve(1000)"
# 100 loops, best of 5: 494 msec per loop (при size = n ** 2)
