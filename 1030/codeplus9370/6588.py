import sys
input = sys.stdin.readline

if __name__=='__main__':
    MAX = 1000000
    primes = [True]*(MAX+1)
    primes[0], primes[1] = False, False
    for i in range(2, int(MAX**0.5)+1):
        primes[i*2::i] = [False]*len(primes[i*2::i])

    while n := int(input()):
        a = 0
        b = n
        flag = False
        while a <= b:
            if primes[a] and primes[b]:
                print(f'{n} = {a} + {b}')
                flag = True
                break
            a += 1
            b -= 1

        if not flag:
            print("Goldbach's conjecture is wrong.")

