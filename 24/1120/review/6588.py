import sys
input = sys.stdin.readline

def create_prime_table():
    global MAX

    prime = [True]*(MAX+1)
    prime[0:2] = [False, False]
    for i in range(2, int((MAX+1)**0.5)):
        if prime[i]:
            prime[i*2::i] = [False]*len(prime[i*2::i])

    return prime

def check_assumption(n, a, b):

    while a <= b:
        if prime[a] and prime[b]:
            return f'{n} = {a} + {b}'
        else:
            a += 1
            b -= 1

    return "Goldbach's conjecture is wrong."

if __name__=='__main__':
    MAX = 1000000
    prime = create_prime_table()

    while True:
        n = int(input())
        if n == 0: break
        print(check_assumption(n, 0, n))
