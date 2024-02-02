#pypy3으로 정답

import sys
input = sys.stdin.readline

CODE_BOOK = {'0': '000', '1': '001',
             '2': '010', '3': '011',
             '4': '100', '5': '101',
             '6': '110', '7': '111'}

if __name__=='__main__':
    num = list(input().rstrip())

    bi = list()
    for n in num:
        bi.append(CODE_BOOK[n])

    print(int(''.join(bi)))
