import sys
input = sys.stdin.readline

from bisect import bisect_left, bisect_right

if __name__=='__main__':

    MAX = 1000000
    prime = [i for i in range(MAX+1)]
    prime[0:2] = [False, False]
    for i in range(2, int(MAX**0.5)+1):
        if prime[i]:
            prime[i*2::i] = [False] * len(prime[i*2::i])

    prime = list(filter(None, prime))

    m, n = map(int, input().rstrip().split())
    l = bisect_left(prime, m)
    r = bisect_right(prime, n)

    for p in prime[l:r]:
        print(p)
