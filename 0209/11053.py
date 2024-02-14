import sys
input = sys.stdin.readline
from bisect import bisect_left

if __name__=='__main__':
    n = int(input())
    nums = list(map(int, input().rstrip().split()))

    x = [nums[0]]
    for i in range(1, n):
        if x[-1] < nums[i]:
            x.append(nums[i])
        else:
            ind = bisect_left(x, nums[i])
            x[ind] = nums[i]

    print(len(x))
