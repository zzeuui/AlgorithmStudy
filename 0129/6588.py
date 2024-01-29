import sys
input = sys.stdin.readline

prime = [True]*1000001
prime[0:2] = [False, False]
for i in range(2, int(1000001**0.5)):
    if prime[i]:
        prime[i+i::i] = [False]*len(prime[i+i::i])

while True:
    n = int(input())
    if n == 0: break

    a, b = 0, n
    while a <= b:
        if prime[a] and prime[b]:
            print(f'{n} = {a} + {b}')
            break

        a += 1
        b -= 1

    if a > b:
        print("Goldbach's conjecture is wrong.")
