# Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

qty = int(input('Введите количество вводимых чисел: '))
numb = input('Введите цифру для подсчета: ')

i = 1
res = ''
ans = 0

while i <= qty:
    n = input(f'Введите число {i}: ')
    res += n
    i += 1

for j in res:
    if j == numb:
        ans += 1

print(f'Цифра {numb} встречается {ans} раз')
