"""
정답 30분 (30분)
"""

import sys
input = sys.stdin.readline

if __name__=='__main__':
    n = int(input())
    nums = []
    ret = []
    for _ in range(n):
        data = list(map(int, input().rstrip().split()))
        nums.append(data)
        ret.append([0]*len(data))

    ret[0][0] = nums[0][0]

    for i in range(1, n):
        for j in range(i+1):
            if j == 0:
                ret[i][j] = nums[i][j] + ret[i-1][j]
            elif j == i:
                ret[i][j] = nums[i][j] + ret[i-1][j-1]
            else:
                ret[i][j] = max(nums[i][j] + ret[i-1][j-1], nums[i][j]+ret[i-1][j])

    print(max(ret[n-1]))
