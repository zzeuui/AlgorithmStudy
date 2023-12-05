import sys
input = sys.stdin.readline

from itertools import permutations

if __name__=='__main__':
    n = int(input())
    nums = list(map(int, input().rstrip().split()))
    nums.sort()

    ret = float('-inf')
    for p in list(permutations(nums)):
        summ = 0
        for i in range(n-1):
            summ += abs(p[i]-p[i+1])

        ret = max(ret, summ)

    print(ret)
