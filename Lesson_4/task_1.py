# Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках
# домашнего задания первых трех уроков.
# Примечание. Идеальным решением будет:
# ● выбрать хорошую задачу, которую имеет смысл оценивать,
# ● написать 3 варианта кода (один у вас уже есть),
# ● проанализировать 3 варианта и выбрать оптимальный,
# ● результаты анализа вставить в виде комментариев в файл с кодом
# (не забудьте указать, для каких N вы проводили замеры),
# ● написать общий вывод: какой из трёх вариантов лучше и почему.

# Проанализируем программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется
# равенство: 1+2+...+n = n(n+1)/2, где n — любое натуральное число
# Примем n = 100

import sys
import cProfile


sys.setrecursionlimit(100000)   # для расширения диапазона тестирования


def main_1(n):

    def sum_row(n):
        if n == 1:
            return 1
        else:
            return n + sum_row(n - 1)

    a = sum_row(n)
    b = n * (n + 1) / 2
    if a == b:
        ans = 'Равенство 1+2+...+n = n(n+1)/2 верно'
    else:
        ans = 'Равенство неверно'


# cProfile.run('main_1(2500)')

# python -m timeit -n 1000 -s "import task_1" "task_1.main_1(500)"
# 1000 loops, best of 5: 88.2 usec per loop
# 500/1    0.001    0.000    0.001    0.001 task_1.py:24(sum_row)

# python -m timeit -n 1000 -s "import task_1" "task_1.main_1(1500)"
# 1000 loops, best of 5: 313 usec per loop
# 1500/1    0.002    0.000    0.002    0.002 task_1.py:24(sum_row)

# python -m timeit -n 1000 -s "import task_1" "task_1.main_1(2500)"
# 1000 loops, best of 5: 563 usec per loop
# 2500/1    0.004    0.000    0.004    0.004 task_1.py:24(sum_row)


def main_2(n):

    def sum_row_memo(n):
        sum_d = {1: 1}

        def _sum_row_memo(n):
            if n in sum_d:
                return sum_d[n]
            sum_d[n] = _sum_row_memo(n - 1) + n
            return sum_d[n]

        return _sum_row_memo(n)

    a = sum_row_memo(n)
    b = n * (n + 1) / 2
    if a == b:
        ans = 'Равенство 1+2+...+n = n(n+1)/2 верно'
    else:
        ans = 'Равенство неверно'


# cProfile.run('main_2(2500)')

# python -m timeit -n 1000 -s "import task_1" "task_1.main_2(500)"
# 1000 loops, best of 5: 138 usec per loop
# 500/1    0.001    0.000    0.001    0.001 task_1.py:56(_sum_row_memo)

# python -m timeit -n 1000 -s "import task_1" "task_1.main_2(1500)"
# 1000 loops, best of 5: 457 usec per loop
# 1500/1    0.002    0.000    0.002    0.002 task_1.py:56(_sum_row_memo)

# python -m timeit -n 1000 -s "import task_1" "task_1.main_2(2500)"
# 1000 loops, best of 5: 751 usec per loop
# 2500/1    0.003    0.000    0.003    0.003 task_1.py:56(_sum_row_memo)


def main_3(n):

    def sum_row_round(n):
        i = 1
        res = 0
        while i <= n:
            res += i
            i += 1
        return res

    a = sum_row_round(n)
    b = n * (n + 1) / 2
    if a == b:
        ans = 'Равенство 1+2+...+n = n(n+1)/2 верно'
    else:
        ans = 'Равенство неверно'


# cProfile.run('main_3(2500)')

# python -m timeit -n 1000 -s "import task_1" "task_1.main_3(500)"
# 1000 loops, best of 5: 40.2 usec per loop
# 1    0.000    0.000    0.000    0.000 task_1.py:85(sum_row_round)

# python -m timeit -n 1000 -s "import task_1" "task_1.main_3(1500)"
# 1000 loops, best of 5: 130 usec per loop
# 1    0.000    0.000    0.000    0.000 task_1.py:85(sum_row_round)

# python -m timeit -n 1000 -s "import task_1" "task_1.main_3(2500)"
# 1000 loops, best of 5: 216 usec per loop
# 1    0.000    0.000    0.000    0.000 task_1.py:85(sum_row_round)

# python -m timeit -n 1000 -s "import task_1" "task_1.main_3(10000)"
# 1000 loops, best of 5: 877 usec per loop

# python -m timeit -n 1000 -s "import task_1" "task_1.main_3(30000)"
# 1000 loops, best of 5: 2.69 msec per loop


def main_4(n):

    def sum_row_round_for(n):
        res = 0
        for itm in range(1, n + 1):
            res += itm
        return res

    a = sum_row_round_for(n)
    b = n * (n + 1) / 2
    if a == b:
        ans = 'Равенство 1+2+...+n = n(n+1)/2 верно'
    else:
        ans = 'Равенство неверно'


# cProfile.run('main_4(2500)')

# python -m timeit -n 1000 -s "import task_1" "task_1.main_4(500)"
# 1000 loops, best of 5: 24.6 usec per loop
# 1    0.000    0.000    0.000    0.000 task_1.py:127(sum_row_round_for)

# python -m timeit -n 1000 -s "import task_1" "task_1.main_4(1500)"
# 1000 loops, best of 5: 76.9 usec per loop
# 1    0.000    0.000    0.000    0.000 task_1.py:127(sum_row_round_for)

# python -m timeit -n 1000 -s "import task_1" "task_1.main_4(2500)"
# 1000 loops, best of 5: 141 usec per loop
# 1    0.000    0.000    0.000    0.000 task_1.py:127(sum_row_round_for)

# python -m timeit -n 1000 -s "import task_1" "task_1.main_4(10000)"
# 1000 loops, best of 5: 538 usec per loop

# python -m timeit -n 1000 -s "import task_1" "task_1.main_4(30000)"
# 1000 loops, best of 5: 1.6 msec per loop


# Зависимость сложности аглоритма от входных данных во всех четырех случаях линейна O(n), но при использовании рекурсии
# время выполнения программы при увеличении входных данных растет быстрее, чем без нее. Поскольку рекурсия вызывает
# только одну копию самой себя в данном случае, то использование мемоизации в main_2(n) не эффективно.
# Так же при использовании рекурсии мы можем упереться в лимит глубины рекурсии. Для решения данной задачи
# наиболее эффективный и быстрый вариант - использование цикла. Цикл "for" эффективнее "while" для данной задачи.
