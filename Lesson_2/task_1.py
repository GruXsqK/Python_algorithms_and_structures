# Написать программу, которая будет складывать, вычитать, умножать или делить два числа.Числа и знак операции
# вводятся пользователем.После выполнения вычисления программа не завершается, а запрашивает новые данные для
# вычислений.Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.Если
# пользователь вводит неверный знак(не '0', '+', '-', '*', '/'), программа должна сообщать об ошибке и снова
# запрашивать знак операции.Также она должна сообщать пользователю о невозможности деления на ноль,
# если он ввел его в качестве делителя.

while True:
    a = float(input('Введите первое число: '))
    b = float(input('Введите второе число: '))
    sign = input('Введите знак операции, 0 для выхода: ')

    if sign == '0':
        break
    elif sign == '/' and b == 0:
        print('Деление на 0 невозможно')
    else:
        if sign == '+':
            print(a + b)
        elif sign == '-':
            print(a - b)
        elif sign == '*':
            print(a * b)
        elif sign == '/':
            print(a / b)
        else:
            print('Неверный знак операции')
