import sys
input = sys.stdin.readline

if __name__=='__main__':
    n = int(input())
    price = list(map(int, input().rstrip().split()))

    dp = [float('inf')]
    dp.extend([p for p in price])

    for i in range(1, n+1):
        for j in range(1, n+1):
            if i+j <= n:
                dp[i+j] = min(dp[i+j], dp[i]+dp[j])

    print(dp[-1])
