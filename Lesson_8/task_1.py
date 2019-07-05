# 1) Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
# Требуется вернуть количество различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.
# Пример работы функции:
#
# func("papa")
# 6
# func("sova")
# 9


import hashlib


def sum_subs(s):
    hs_s = hashlib.sha1(s.encode('utf-8')).hexdigest()
    set_hs_subs = set()
    ln_s = len(s)

    for idx, _ in enumerate(s):
        n = 1
        while idx + n < ln_s + 1:
            set_hs_subs.add(hashlib.sha1(s[idx:idx + n].encode('utf-8')).hexdigest())
            n += 1

    set_hs_subs.discard(hashlib.sha1(''.encode('utf-8')).hexdigest())
    set_hs_subs.discard(hs_s)

    return len(set_hs_subs)


print(sum_subs('War and Peace!'))
