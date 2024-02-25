import sys
input = sys.stdin.readline

if __name__=='__main__':
    n = int(input())
    nums = list(map(int, input().rstrip().split()))
    dp = nums[:]
    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i] and dp[i] < dp[j]+nums[i]:
                dp[i] = dp[j]+nums[i]

    print(max(dp))