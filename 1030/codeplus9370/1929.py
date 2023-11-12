import sys
input = sys.stdin.readline
from bisect import bisect_left, bisect_right

if __name__=='__main__':
    MAX = 1000000
    primes = [i for i in range(MAX+1)]
    primes[0], primes[1] = 0, 0
    for i in range(2, int(MAX**0.5)+1):
        primes[i*2::i] = [0]*len(primes[i*2::i])
    
    primes = list(filter(None, primes))

    m, n = map(int, input().rstrip().split())
    primes = primes[bisect_left(primes, m):bisect_right(primes, n)]
    for p in primes:
        print(p)
