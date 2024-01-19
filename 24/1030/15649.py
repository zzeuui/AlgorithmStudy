import sys
input = sys.stdin.readline
from itertools import permutations

if __name__=='__main__':
    n, m = map(int, input().rstrip().split())
    nums = [i for i in range(1, n+1)]*m

    for p in list(permutations(nums, m)):
        print(' '.join([str(num) for num in p]))
