import sys
input = sys.stdin.readline

def compute_gcd(n, m):
    while m != 0:
        r = n%m
        n, m = m, r

    return n

if __name__=='__main__':
    n, s = map(int, input().rstrip().split())
    a = list(map(int, input().rstrip().split()))

    a = [abs(i - s) for i in a]

    if len(a) == 1:
        print(a[0])
    else:
        for i in range(len(a)-1):
            a[i+1] = compute_gcd(a[i], a[i+1])


        print(a[-1])
