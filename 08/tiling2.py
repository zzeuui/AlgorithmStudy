
def f(n):
    if n <= 1: return 1
    if cache[n] < 0: cache[n] = (f(n-2) + f(n-1)) % 1000000007
    return cache[n]

if __name__=='__main__':
    case_n = int(input())

    for _ in range(case_n):
        n = int(input())
        cache = [-1]*101
        print(f(n))

