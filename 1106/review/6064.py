import sys
input = sys.stdin.readline

if __name__=='__main__':
    for _ in range(int(input())):
        m, n, x, y = map(int, input().rstrip().split())

        flag = False
        k = x
        while k <= m*n:

            if (k-x)%m==0 and (k-y)%n==0:
                flag  = True
                break

            k += m

        if flag:
            print(k)
        else:
            print(-1)
