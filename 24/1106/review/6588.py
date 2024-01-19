import sys
input = sys.stdin.readline

from bisect import bisect_left, bisect_right

if __name__=='__main__':

    MAX = 1000000
    prime = [True]*(MAX+1)
    prime[0:2] = [False, False]
    for i in range(2, int(MAX**0.5)+1):
        if prime[i]:
            prime[i*2::i] = [False] * len(prime[i*2::i])

    while True:
        n = int(input())
        if n == 0:
            break

        a = 0
        b = n
        flag = False
        while a <= b:
            if prime[a] and prime[b]:
                print(f'{n} = {a} + {b}')
                flag = True
                break
            else:
                a += 1
                b -= 1

        if not flag:
            print("Goldbach's conjecture is wrong.")
