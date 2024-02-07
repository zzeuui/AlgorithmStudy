#그 매트릭스에서 비용 계산하는 거라 비슷한 것 같다
import sys
input = sys.stdin.readline

if __name__=='__main__':
    n = int(input())
    price = list(map(int, input().rstrip().split()))

    dp = [0]
    dp.extend([p for p in price])
    
    """
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i+j == n:
                dp[n] = max(dp[n], dp[i]+dp[j])
    """

    for i in range(1, n+1):
        for j in range(1, n+1):
            if i+j <= n:
                dp[i+j] = max(dp[i+j], dp[i]+dp[j])

    print(dp[-1])
