"""
MOD = 10*1000*1000

def poly(n, first):

    k = n*10+first

    if n == first: return 1

    if cache[k] < 1:
        for second in range(1, n-first+1):
            cache[k] += ((second+first-1)*poly(n-first, second))

    return cache[k]

if __name__=='__main__':
    for _ in range(int(input())):
        n = int(input())
        cache = [0]*1100
        summ = 0
        for i in range(1, n+1):
            summ += poly(n, i) 

        print(summ%MOD)

"""

from functools import lru_cache

@lru_cache(maxsize=None)
def poly(N, first):
    if first == N:
        return 1
    return sum((first+i-1) * poly(N-first, i) for i in range(1, N-first+1))

if __name__=='__main__':
    for case in range(int(input())):
        N = int(input())
        print(sum(poly(N, i) for i in range(1, N+1)) % 10000000)

# lru_cache:
# https://docs.python.org/ko/3/library/functools.html

