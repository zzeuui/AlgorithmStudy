import sys
input = sys.stdin.readline

if __name__=='__main__':

    dp = [0]*12
    dp[0:4] = [0, 1, 2, 4]
    for i in range(4, 12):
        dp[i] = dp[i-3] + dp[i-2] + dp[i-1]

    for _ in range(int(input())):
        n = int(input())
        print(dp[n])
