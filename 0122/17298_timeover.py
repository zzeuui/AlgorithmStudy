import sys
input = sys.stdin.readline
import bisect

if __name__=='__main__':
    n = int(input())
    nums = list(map(int, input().rstrip().split()))

    ret = list()
    while nums:
        i = nums.pop(0)
        temp = sorted(nums)
        ind = bisect.bisect_left(temp, i)

        if ind < len(temp):
            ret.append(temp[ind])
        else:
            ret.append(-1)

    print(' '.join(list(map(str, ret))))
