# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.


def count_aliquot_numb(numb_list, numb):
    i = 0
    num_count = 0
    while i < len(numb_list):
        if numb != 0 and numb_list[i] % numb == 0:
            num_count += 1
        i += 1
    return num_count


MIN_NUMB_LIST = 2
MAX_NUMB_LIST = 99
MIN_NUMB_ALIQUOT = 2
MAX_NUMB_ALIQUOT = 9

num_list = [itm for itm in range(MIN_NUMB_LIST, MAX_NUMB_LIST + 1)]

for itm in range(MIN_NUMB_ALIQUOT, MAX_NUMB_ALIQUOT + 1):
    print(f'Число {itm} кратно {count_aliquot_numb(num_list, itm)} числам')
