# Для каждого упражнения написать программную реализацию.
# Код пишите в файлах с расширением .py в кодировке UTF-8 (в PyCharm работает по умолчанию).Каждую задачу необходимо
# сохранять в отдельный файл. Рекомендуем использовать английские имена, например, les_6_task_1.
# Для оценки «Отлично» необходимо выполнить все требования, указанные в задании и примечаниях.
# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:
# ● выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
# ● написать 3 варианта кода (один у вас уже есть);
# ● проанализировать 3 варианта и выбрать оптимальный;
# ● результаты анализа (количество занятой памяти в вашей среде разработки) вставить в виде комментариев в файл
# с кодом. Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;
# ● написать общий вывод: какой из трёх вариантов лучше и почему. Надеемся, что вы не испортили программы,
# добавив в них множество sys.getsizeof после каждой переменной, а проявили творчество, фантазию
# и создали универсальный код для замера памяти.

# Задача: определить, какое число в массиве встречается чаще всего.


import sys
from collections import Counter
import random


MIN_NUMB = 0
MAX_NUMB = 1000
COUNT_NUMB = 5000


def size_of_memory(dct_vars):

    sum_size = 0
    for value in dct_vars.values():
        sum_size += sys.getsizeof(value, default=0)
        try:
            if type(value) in (dict, Counter):
                for itm in value.items():
                    sum_size += sys.getsizeof(itm, default=0)
            elif not isinstance(value, str):
                pass
            else:
                for itm in value:
                    sum_size += sys.getsizeof(itm, default=0)
        except TypeError:
            pass

    return sum_size


def task_edition_1():

    random.seed(COUNT_NUMB)     # для сравнения вариантов при одинаковых данных
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

    res = f'Число {num_max_count} встречается чаще всего ({max_count} раз)'
    size_mem = size_of_memory(locals())

    return size_mem


def task_edition_2():

    random.seed(COUNT_NUMB)
    num_count = Counter(list(random.randint(MIN_NUMB, MAX_NUMB) for _ in range(COUNT_NUMB)))
    ans = num_count.most_common(1)
    res = f'Число {ans[0][0]} встречается чаще всего ({ans[0][1]} раз)'
    size_mem = size_of_memory(locals())

    return size_mem


def task_edition_2_2():

    random.seed(COUNT_NUMB)
    ans = Counter(list(random.randint(MIN_NUMB, MAX_NUMB) for _ in range(COUNT_NUMB))).most_common(1)
    res = f'Число {ans[0][0]} встречается чаще всего ({ans[0][1]} раз)'
    size_mem = size_of_memory(locals())

    return size_mem


def task_edition_3():

    random.seed(COUNT_NUMB)
    num_lst = list(random.randint(MIN_NUMB, MAX_NUMB) for _ in range(COUNT_NUMB))
    num_lst.sort()
    spam = None
    i = 0
    ans_count = 0
    ans_numb = None

    for elm in num_lst:
        if elm != spam:
            spam = elm
            i = 1
        else:
            i += 1

        if i > ans_count:
            ans_count = i
            ans_numb = elm

    res = f'Число {ans_numb} встречается чаще всего ({ans_count} раз)'
    size_mem = size_of_memory(locals())

    return size_mem


# Python: 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)]
# OS: ('64bit', 'WindowsPE')
# Выделенная память под константы = 80
# Выделенная память под одну функцию (без объектов внутри) = 28


# При MIN_NUMB = 0, MAX_NUMB = 100, COUNT_NUMB = 500
# size of vars in task_edition_1() = 18210          100 loops, best of 5: 954 usec per loop
# size of vars in task_edition_2() = 14138          100 loops, best of 5: 710 usec per loop
# size of vars in task_edition_2_2() = 2954         100 loops, best of 5: 668 usec per loop
# size of vars in task_edition_3() = 7598          100 loops, best of 5: 882 usec per loop
#
# При MIN_NUMB = 0, MAX_NUMB = 100, COUNT_NUMB = 50000
# size of vars in task_edition_1() = 414262        100 loops, best of 5: 89.4 msec per loop
# size of vars in task_edition_2() = 14190          100 loops, best of 5: 66.1 msec per loop
# size of vars in task_edition_2_2() = 3006         100 loops, best of 5: 65 msec per loop
# size of vars in task_edition_3() = 436890        100 loops, best of 5: 91.6 msec per loop

# При MIN_NUMB = 0, MAX_NUMB = 10000, COUNT_NUMB = 500
# size of vars in task_edition_1() = 56726          100 loops, best of 5: 1.18 msec per loop
# size of vars in task_edition_2() = 52654          100 loops, best of 5: 954 usec per loop
# size of vars in task_edition_2_2() = 3006         100 loops, best of 5: 773 usec per loop
# size of vars in task_edition_3() = 7598          100 loops, best of 5: 947 usec per loop

print('Память для task_edition_1 =', task_edition_1())           # te_1
print('Память для task_edition_2 =', task_edition_2())           # te_2
print('Память для task_edition_2_2 =', task_edition_2_2())       # te_2_2
print('Память для task_edition_3 =', task_edition_3())           # te_3

# Самым быстрым и оптимальным по использованию памяти (среди вышенаписанных) является алгоритм te_2_2,
# при изменении размеров массива и порядка значений в нем, объем памяти для хранения объектов практически не менялся,
# но при расчетах алгоритм te_2_2 будет использовать те же ресурсы, что и te_2, для хранения промежуточных значений.
# Алгоритм te_2 не увеличивает "потребление" памяти при увеличении количества переменных (при хранении), но увеличивает
# при большем разбросе значений переменных, это вызвано использованием Counter'а, который растет в размерах быстрее
# при большем диапазоне значений переменных. В алгоритме te_1 при увеличении количества переменыых растет в размерах
# кортеж (и немного словарь из-за увеличения вероятности появления определенного числа), а при увеличении
# диапазона - только словарь. Алгоритм te_3 не требует больше памяти при увеличении диапазона значений, за счет
# использования переменных, но увеличивается время выполнения при увеличении размеров массива из-за сортировки.
