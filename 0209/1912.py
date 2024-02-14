import sys
input = sys.stdin.readline

if __name__=='__main__':
    n = int(input())
    nums = list(map(int, input().rstrip().split()))

    dp = [nb for nb in nums]

    for i in range(1, n):
        dp[i] = max(dp[i], dp[i]+dp[i-1])

    print(max(dp))



