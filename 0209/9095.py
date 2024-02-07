import sys
input = sys.stdin.readline

if __name__=='__main__':

    dp = [0]*(11+1)
    dp[:3] = [1, 2, 4]
    for _ in range(int(input())):
        n = int(input())
        for i in range(3, n):
            dp[i] = dp[i-3] + dp[i-2] + dp[i-1]

        print(dp[n-1])
