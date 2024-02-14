import sys
input = sys.stdin.readline

if __name__=='__main__':
    n = int(input())
    nums = list(map(int, input().rstrip().split()))

    dp = [1]*(n+1)

    for i in range(len(nums)):
        for j in range(i):
            #if front number is smaller than current number
            if nums[j] <  nums[i]:
                #to come to current number..
                #distance to current number vs. distance throught front number+1
                dp[i] = max(dp[i], dp[j]+1) 

    #length of the largest subsets
    x = max(dp)
    print(x)
    ret = list()
    for i in range(n-1, -1, -1):
        if dp[i] == x:
            ret.append(nums[i])
            x -= 1

    ret.reverse()
    print(*ret)
