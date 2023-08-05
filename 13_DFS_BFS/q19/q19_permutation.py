"""
정답 (1시간 37분)

dfs로 풀어보려고 했다가 순열로 품
시간 3784ms.. 채점하는데 오래걸림
"""
from itertools import permutations
import sys
input = sys.stdin.readline

def compute(op):
    n1 = num[0]
    for o, n2 in zip(op, num[1:]):
        if o == 0:
            n1 += n2
        elif o == 1:
            n1 -= n2
        elif o == 2:
            n1 *= n2
        elif o == 3:
            if n1 < 0:
                n1 = abs(n1) // n2
                n1 *= -1
            else:
                n1 //= n2

    return n1

n = int(input())
num = list(map(int, input().split()))
op_info = list(map(int, input().split()))
opert = list()
for i, op_info in enumerate(op_info):
    for _ in range(op_info):
        opert.append(i)

ret = defaultdict(int) 
for op in list(permutations(opert)):
    ret.append(compute(op))

ret.sort()
print(ret[-1])
print(ret[0])
