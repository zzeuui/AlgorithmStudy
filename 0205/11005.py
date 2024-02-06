import sys
input = sys.stdin.readline

if __name__=='__main__':
    n, b = map(int, input().rstrip().split())

    ret = list()
    while n != 0:
        ret.append(n%b)
        print(n, n%b)
        n = n//b

    ret = [chr(55+n) if n > 9 else str(n) for n in ret][::-1]
    print(''.join(ret))
