import sys
input = sys.stdin.readline

from bisect import bisect_left

if __name__=='__main__':
    MAX = 1000000

    prime_list = list(range(MAX+1)) # [0, 1, ..., MAX-1, MAX]
    prime_list[1] = 0
    for i in range(2, int(MAX**0.5)+1): # the sieve of eratosthenes
        if prime_list[i]: #i-th is prime number
            """
            i+i = i*2
            [i+i:] = from i*2
            [::i] = every i
            [i+i::i] = from i*2, every i..
            ex1) i=2, [4, 6, 8, ..., n*2(n*i)]
            ex2) i=3, [6, 9, 12, ..., n*3(n*i)]
            """
            prime_list[i+i::i] = [0] *len(prime_list[i+i::i])

    # if the element is 0, False, None.. delete it in the list
    # prime_list = list(filter(None, prime_list[2:]))

    while n := int(input()):
        flag = False

        a = 0
        b = n
        
        while a <= b:
            if prime_list[a] and prime_list[b]:
                print(f'{n} = {prime_list[a]} + {prime_list[b]}')
                flag = True
                break
            else:
                a += 1
                b -= 1

        if not flag:
            print("Goldbach's conjecture is wrong.")
