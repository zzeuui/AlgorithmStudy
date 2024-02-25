import sys
input = sys.stdin.readline

N = int(input())
input_array = list(map(int, input().split()))
dp = [[x for x in input_array] for _ in range(2)]

for i in range(1, N):
    #특정 원소를 제거하지 않은 경우
    dp[0][i] = max(dp[0][i - 1] + input_array[i], dp[0][i])
    #특정 원소를 제거하는 경우
    dp[1][i] = max(dp[0][i - 1], #i번째 원소를 제거하거나
                   dp[1][i - 1] + input_array[i])# 그전에dp에 저장된 특정 원소를 제거한 값에 이 원소를 더하거나

print(max(max(dp[0]), max(dp[1])))
