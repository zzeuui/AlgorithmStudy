import sys
input = sys.stdin.readline

import math

if __name__=='__main__':
    n = int(input())

    ret = list()
    if n == 0:
        print(0)
    else:
        while n:
            ret.append(str(abs(n%-2)))
            n = math.ceil(n/-2)

        print(''.join(ret[::-1]))
