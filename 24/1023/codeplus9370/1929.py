MAX = 1000000
dp = [n for n in range(MAX+1)]
dp[1] = 0
for i in range(2, int(MAX**0.5)+1):
    dp[i+i::i] = [0]*len(dp[i+i::i])

dp = list(filter(None, dp))
n, m = map(int, input().split())

from bisect import bisect_left, bisect_right

n_ind = bisect_left(dp, n)
m_ind = bisect_right(dp, m)
for e in dp[n_ind:m_ind]:
    print(e)
