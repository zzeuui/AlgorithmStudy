mport sys
input = sys.stdin.readline
from itertools import permutations

if __name__=='__main__':
    n, m = map(int, input().rstrip().split())
    nums = [i for i in range(1, n+1)]
    permt = [sorted(list(p)) for p in list(permutations(nums, m))]
    permt = [' '.join([str(num) for num in p]) for p in permt]
    permt = sorted(list(set(permt)))

    for p in permt:
        print(p)
