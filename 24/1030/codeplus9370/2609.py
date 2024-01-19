import sys
input = sys.stdin.readline

if __name__=='__main__':
    n, m = map(int, input().rstrip().split())
    minv, maxv = min(n, m), max(n, m)
    
    r1 = minv
    while True:
        if n % r1 == 0 and m % r1 == 0:
            break
        r1 -= 1

    r2 = maxv
    i = 1
    while True:
        if r2*i % minv == 0:
            break
        i += 1

    print(r1)
    print(r2*i)
