import sys
input = sys.stdin.readline

if __name__=='__main__':
    for _ in range(int(input())):
        n = int(input())
        if n == 1:
            print(1)
        elif n == 2:
            print(2)
        elif n == 3:
            print(4)
        else:
            dp = [0]*(n+1)
            dp[1] = 1
            dp[2] = 2
            dp[3] = 4

            for i in range(4, n+1):
                dp[i] = sum(dp[i-3:i])

            print(dp[n])
