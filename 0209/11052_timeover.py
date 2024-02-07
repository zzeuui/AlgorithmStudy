import sys
input = sys.stdin.readline

def f(n, p):
    global ret

    if n == 0:
        ret = max(ret, p)

    for i in range(1, n+1):
        if n-i >= 0:
            f(n-i, p+price[i-1])

if __name__=='__main__':
    n = int(input())
    price = list(map(int, input().rstrip().split()))

    ret = 0
    f(n, 0)
    print(ret)
