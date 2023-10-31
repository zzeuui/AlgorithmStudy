import sys
input = sys.stdin.readline

if __name__=='__main__':
    e, s, m = map(int, input().rstrip().split())

    ret = 0
    i, j, k = 1, 1, 1
    while True:
        ret += 1
        if i == e and s == j and m == k:
            break

        if i <15:
            i += 1
        else:
            i = 1

        if j < 28:
            j += 1
        else:
            j = 1

        if k < 19:
            k += 1
        else:
            k = 1

    print(ret)
