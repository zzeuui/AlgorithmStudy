import sys
input = sys.stdin.readline

if __name__=='__main__':
    num = int(input())

    dp = [float('inf')]*(num+1)
    dp[num] = 0

    for n in range(1, num+1)[::-1]:
        if n%3 == 0:
            dp[n//3] = min(dp[n]+1, dp[n//3])

        if n%2 == 0:
            dp[n//2] = min(dp[n]+1, dp[n//2])

        dp[n-1] = min(dp[n]+1, dp[n-1])

    print(dp[1])
