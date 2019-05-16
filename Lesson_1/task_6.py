
# Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

num = int(input('Введите номер буквы: '))

first_ch = ord('a')
let = chr(num + first_ch - 1)

print(let)
