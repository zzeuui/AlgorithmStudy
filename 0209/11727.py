import sys
input = sys.stdin.readline

if __name__=='__main__':
    n = int(input())
    
    dp = [0]*n
    dp[:2] = [1, 3]

    for i in range(2, n):
        dp[i] = 2*dp[i-2] + dp[i-1]

    print(dp[n-1]%10007)
