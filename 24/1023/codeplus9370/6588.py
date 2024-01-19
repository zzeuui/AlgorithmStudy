import sys
input = sys.stdin.readline

if __name__=='__main__':
    MAX = 1000000
    dp = [True]*(MAX+1)
    dp[0], dp[1] = False, False
    for i in range(2, int(MAX**0.5)+1):
        dp[i+i::i] = [False]*len(dp[i+i::i])

    while n := int(input()):
        a = 0
        b = n
        f = False
        while a <= b:
            if dp[a] and dp[b]:
                f = True
                break
            else:
                a += 1
                b -= 1

        if f:
            print(f'{n} = {a} + {b}')
        else:
            print("Goldbach's conjecture is wrong.")
