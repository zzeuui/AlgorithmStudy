n = int(input())

dp = [i for i in range(n+1)]

for i in range(2, n+1):
    for j in range(1, i+1):
        s = j**2
        if s > i:
            break

        if dp[i] > dp[i-s]+1:
            dp[i] = dp[i-s] + 1

print(dp[n])
