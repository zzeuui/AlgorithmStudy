MOD = 1000000007

def d(n):
    if n%2 == 1:
        return (f(n)-f(int(n/2))+MOD)%MOD

    ret = f(n)
    ret -= f(int(n/2))+MOD
    ret = ret%MOD
    ret -= f(int(n/2-1))+MOD

    return ret%MOD

def f(n):
    if n <= 1: return 1
    if cache[n] < 0: cache[n] = (f(n-2) + f(n-1)) % MOD
    return cache[n]

if __name__=='__main__':
    case_n = int(input())

    for _ in range(case_n):
        n = int(input())
        cache = [-1]*101
        print(d(n))

