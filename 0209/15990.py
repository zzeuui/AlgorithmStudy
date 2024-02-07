import sys
input = sys.stdin.readline

"""
- 시간 초과됨 
if __name__=='__main__':

    for _ in range(int(input())):
        n = int(input())
        
        dp = [0]*(n+1)

        dp[1] = [0, 0, 1]
        dp[2] = [0, 1, 0]
        dp[3] = [1, 1, 1]

        for i in range(4, n+1):
            dp[i] = [(sum(dp[i-3]) - dp[i-3][0])%1000000009,
                     (sum(dp[i-2]) - dp[i-2][1])%1000000009,
                     (sum(dp[i-1]) - dp[i-1][2])%1000000009]

        print(sum(dp[-1])%1000000009)

        for i in range(4, n+1):
            dp[i] = [(dp[i-3][1] + dp[i-3][2])%1000000009,
                     (dp[i-2][0] + dp[i-2][2])%1000000009,
                     (dp[i-1][0] + dp[i-1][1])%1000000009]

        print(sum(dp[-1])%1000000009)
"""

if __name__=='__main__':
    NUM = 100001
    dp = [0]*NUM

    dp[1] = [0, 0, 1]
    dp[2] = [0, 1, 0]
    dp[3] = [1, 1, 1]


    for i in range(4, NUM):
        dp[i] = [(dp[i-3][1] + dp[i-3][2])%1000000009,
                 (dp[i-2][0] + dp[i-2][2])%1000000009,
                 (dp[i-1][0] + dp[i-1][1])%1000000009]

    for _ in range(int(input())):
        print(sum(dp[n])%1000000009)
