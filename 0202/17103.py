# pypy3으로 정답
import sys
input = sys.stdin.readline

if __name__=='__main__':

    MAX = 1000000
    prime = [True]*(MAX+1)
    prime[:2] = [False, False]

    for i in range(2, int((MAX+1)**0.5)):
        if prime[i]:
            prime[i*2::i] = [False]*len(prime[i*2::i])

    for _ in range(int(input())):
        n = int(input())
        a, b = 0, n

        cnt = 0
        while a <= b:
            if prime[a] and prime[b]:
                cnt += 1

            a += 1
            b -= 1

        print(cnt)
