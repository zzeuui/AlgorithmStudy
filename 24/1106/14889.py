import sys
input = sys.stdin.readline

from itertools import combinations

def f(t):

    ret = 0
    for _ in range(len(t)):
        i = t.pop(0)
        for j in t:
            ret += scores[i][j]
        t.append(i)

    return ret

if __name__=='__main__':
    n = int(input())
    scores = [list(map(int, input().rstrip().split())) for _ in range(n)]
    nums = [i for i in range(n)]

    can_t1 = list(combinations(nums, n//2))

    ret = float('inf')
    for t1 in can_t1[:len(can_t1)//2]:
        t2 = set(nums) - set(t1)
        ret = min(ret, abs(f(list(t1))-f(list(t2))))
    print(ret)

