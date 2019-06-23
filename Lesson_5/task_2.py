# Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется
# как массив, элементы которого — цифры числа. Например, пользователь ввёл A2 и C4F. Нужно сохранить их как
# [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
# произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].


from collections import deque


def math_hex(num_1, num_2, sig):

    hex_tuple = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F',)

    def sum_hex(num_1, num_2):

        sum_deq = deque()

        if len(num_1) < len(num_2):
            num_1, num_2 = num_2, num_1

        flag = 0
        while len(num_2) > 0:
            idx_sum = hex_tuple.index(num_1.pop()) + hex_tuple.index(num_2.pop()) + flag

            if idx_sum > 15:
                flag = 1
                idx_sum -= 16
            else:
                flag = 0
            sum_deq.appendleft(hex_tuple[idx_sum])

        if flag != 0:
            if len(num_1) != 0:
                num_1 = sum_hex(num_1, deque(str(flag)))
            else:
                num_1.appendleft(str(flag))

        sum_deq = num_1 + sum_deq
        return sum_deq

    def mult_hex(num_1, num_2):

        if len(num_1) < len(num_2):
            num_1, num_2 = num_2, num_1

        shift = 0
        res = deque('0')
        while len(num_2) > 0:
            mlt = hex_tuple.index(num_2.pop())
            mlt_numb = deque()

            for _ in range(mlt):
                mlt_cop = num_1.copy()
                mlt_numb = sum_hex(mlt_numb, mlt_cop)

            for _ in range(shift):
                mlt_numb.append('0')

            res = sum_hex(mlt_numb, res)
            shift += 1

        return res

    if sig == '+':
        return sum_hex(num_1, num_2)
    elif sig == '*':
        return mult_hex(num_1, num_2)
    else:
        return f'Операции не существует ({sig})'


num_1 = deque((input('Введите первое число в Hex: ')).upper())
num_2 = deque((input('Введите второе число в Hex: ')).upper())
sig = input('Введите знак операции: ')
print(math_hex(num_1, num_2, sig))
