import sys
input = sys.stdin.readline
from itertools import combinations

if __name__=='__main__':
    heights = [int(input()) for _ in range(9)]
    candi = list(combinations(heights, 7))
    for c in candi:
        if sum(c) == 100:
            break

    c = sorted(list(c))
    for n in c:
        print(n)
