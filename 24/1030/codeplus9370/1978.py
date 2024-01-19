import sys
input = sys.stdin.readline

if __name__=='__main__':
    MAX = 1000
    primes = [True]*(MAX+1)
    primes[0], primes[1] = False, False
    for i in range(2, int(MAX**0.5)+1):
        if primes[i]:
            j = 2
            while i*j < MAX+1:
                primes[i*j] = False
                j += 1

    n = int(input())
    nums = list(map(int, input().rstrip().split()))
    ret = 0
    for n in nums:
        if primes[n]:
            ret += 1
    print(ret)
