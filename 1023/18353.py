import sys
input = sys.stdin.readline

from bisect import bisect_left

if __name__=='__main__':
    n = int(input())
    nums = list(map(int, input().rstrip().split()))

    nums = nums[::-1]

    x = [nums[0]]

    for e in nums[1:]:
        
        if e > x[-1]:
            x.append(e)
        else:
            ind = bisect_left(x, e)
            x[ind] = e

    print(n-len(x))
