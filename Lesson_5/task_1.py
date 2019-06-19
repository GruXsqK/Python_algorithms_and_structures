# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа)
# для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести
# наименования предприятий, чья прибыль выше среднего и ниже среднего.


from collections import namedtuple


num_firms = int(input('Введите количество предприятий: '))
Firm = namedtuple('Firm', 'name quart_1 quart_2 quart_3 quart_4 year')
firms_lst = {}
sum_avg = 0

for itm in range(1, num_firms + 1):
    name = input(f'Введите имя {itm}-го предприятия: ')
    quarts = {}
    sum_quarts = 0

    for value in range(1, 5):
        quarts[value] = float(input(f'Введите прибыль {itm}-го предприятия за {value} квартал: '))
        sum_quarts += quarts[value]

    sum_avg += sum_quarts
    firms_lst[itm] = Firm(name, quarts[1], quarts[2], quarts[3], quarts[4], sum_quarts)

sum_avg /= num_firms
ab_avg_year = []
bl_avg_year = []

for key in firms_lst:
    if firms_lst[key].year > sum_avg:
        ab_avg_year.append(firms_lst[key].name)
    elif firms_lst[key].year < sum_avg:
        bl_avg_year.append(firms_lst[key].name)

print(f'Средняя прибыль за год: {sum_avg}')
print('Предприятия с выручкой выше среднего:')
for itm in ab_avg_year:
    print(itm)
print('Предприятия с выручкой ниже среднего:')
for itm in bl_avg_year:
    print(itm)
