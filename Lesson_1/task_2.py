
# Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.

a = 5
b = 6

c = a & b
d = a | b
e = a ^ b
f = ~ a
a_right = a >> 2
a_left = a << 2

print(f'a & b = {c}\na | b = {d}\na ^ b = {e}\n~ a = {f}\n'
      f'побитовый сдвиг вправо на 2 числа a = {a_right}\nпобитовый сдвиг влево на 2 числа a = {a_left}')
