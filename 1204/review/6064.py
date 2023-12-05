import sys
input = sys.stdin.readline

def count_year(m,n,x,y):

    k = x
    while m*n >= k:
        if (k-x)%m == 0 and (k-y)%n == 0:
            return k

        k += m

    return -1

if __name__=='__main__':
    for _ in range(int(input())):
        m, n, x, y = map(int, input().rstrip().split())
        print(count_year(m,n,x,y))
