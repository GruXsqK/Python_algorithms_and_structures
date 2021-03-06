
# По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b,
# проходящей через эти точки.

x_1 = int(input('Введите x_1:'))
y_1 = int(input('Введите y_1:'))
x_2 = int(input('Введите x_2:'))
y_2 = int(input('Введите y_2:'))

if x_1 == x_2:
    ans = f'x = {x_1}'
elif y_1 == y_2:
    ans = f'y = {y_1}'
else:
    k = (y_2 - y_1) / (x_2 - x_1)
    b = y_1 - k * x_1

    if b >= 0:
        ans = f'y = {k} x + {b}'
    else:
        ans = f'y = {k} x - {abs(b)}'

print(ans)
