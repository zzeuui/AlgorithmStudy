"""
https://velog.io/@yje876/python%EB%B0%B1%EC%A4%80DP-2133-%ED%83%80%EC%9D%BC-%EC%B1%84%EC%9A%B0%EA%B8%B0
"""
n = int(input())
dp = [0 for _ in range(31)]
dp[2] = 3
for i in range(4,n+1) :
    if i%2 == 0 :
        dp[i] = dp[i-2] * 3 + sum(dp[:i-2]) * 2 + 2
    else :
        dp[i] = 0
print(dp[n])