import sys
input = sys.stdin.readline

if __name__=='__main__':
    n = int(input())
    nums = list(map(int, input().rstrip().split()))
    dp = [1]*n
    for i in range(1, n):
        for j in range(i):
            if nums[j] > nums[i] and dp[i] < dp[j]+1:
                dp[i] = dp[j]+1

    print(max(dp))
