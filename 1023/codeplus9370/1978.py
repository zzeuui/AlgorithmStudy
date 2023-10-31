import sys
input = sys.stdin.readline

MAX = 1000
dp = [True]*(MAX+1)
dp[0], dp[1] = False, False
for i in range(2, MAX+1):
    dp[i+i::i] = [False]*len(dp[i+i::i])

n = int(input())
nums = list(map(int, input().rstrip().split()))
nums = [x for x in nums if dp[x]]
print(len(nums))
