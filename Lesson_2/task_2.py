# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5)

a = input('Введите натуральное число: ')
odd = 0
even = 0

for n in a:
    if int(n) % 2 == 0:
        even += 1
    else:
        odd += 1

print(f'В числе {even} четных и {odd} нечетных цифр')
