import sys
input = sys.stdin.readline

if __name__=='__main__':
    n = int(input())
    nums = list(map(int, input().rstrip().split()))
    dp_inc = [1]*n
    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i] and dp_inc[i] < dp_inc[j]+1:
                dp_inc[i] = dp_inc[j]+1

    dp_dec = [1]*n
    nums = nums[::-1]
    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i] and dp_dec[i] < dp_dec[j]+1:
                dp_dec[i] = dp_dec[j]+1
    dp_dec = dp_dec[::-1]

    ret = list()
    for i in range(n-1):
        ret.append(dp_inc[i]+max(dp_dec[i+1:]))

    print(max(ret))
