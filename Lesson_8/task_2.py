# 2) Закодируйте любую строку по алгоритму Хаффмана.


from collections import Counter


class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def walk(self, dct, acc):
        if self.left or self.right:
            self.left.walk(dct, acc + "0")
            self.right.walk(dct, acc + "1")
        else:
            dct[self.value] = acc or "0"


def huffman_dct(st):
    if not len(st):
        return None

    cnt = Counter()

    for itm, freq in Counter(st).items():
        cnt += Counter({Node(value=itm): freq})

    while len(cnt) > 1:
        elm1 = cnt.most_common()[-1]
        cnt[elm1[0]] = 0
        cnt += Counter()
        elm2 = cnt.most_common()[-1]
        cnt[elm2[0]] = 0
        cnt += Counter()
        cnt += Counter({Node(left=elm1[0], right=elm2[0]): elm1[1] + elm2[1]})

    huff_dct = {}
    list(cnt.elements())[0].walk(huff_dct, "")

    return huff_dct


def huffman_encode(st):
    dct = huffman_dct(st)
    code = ''
    for itm in st:
        code += dct[itm]

    return code


def huffman_decode(code, dct):
    st = ''
    ch = ''
    for itm in code:
        ch += itm
        for key, value in dct.items():
            if ch == value:
                st += key
                ch = ''
                break

    return st


if __name__ == '__main__':

    s = 'beep boop beer!'
    print(' '.join(format(ord(i), 'b') for i in s))
    spam = huffman_dct(s)
    eggs = huffman_encode(s)
    print(eggs)
    print(huffman_decode(eggs, spam))
