import sys
input = sys.stdin.readline

if __name__=='__main__':
    n = int(input())
    nums = list(map(int, input().rstrip().split()))

    dp = [nb for nb in nums]
    for i in range(1, n):
        dp[i] = max(dp[i], dp[i]+dp[i-1])

    ret = max(dp)

    for ind in range(n):
        dp2 = [nb for nb in nums]
        dp2.pop(ind)
        for i in range(1, n-1):
            dp2[i] = max(dp2[i], dp2[i]+dp2[i-1])
        ret = max(ret, max(dp2))

    print(ret)