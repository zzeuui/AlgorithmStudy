"""
from functools import lru_cache
@lru_cache(maxsize=None)
def sub(n, i):
    n -= arr[i]
    if n == 0: return 1
    if n < 0: return 0
    return sub(n,0) + sub(n, 1)

if __name__=='__main__':
    n = int(input())
    arr = [1, 2]
    m = sub(n, 0) + sub(n, 1)
    print(m%15746)
"""

if __name__=='__main__':
    n = int(input()) + 1
    f = [1]*n
    for i in range(2, n):
        f[i] = (f[i-1]+f[i-2])%15746

    print(f[n-1])
