import sys
input = sys.stdin.readline

from itertools import combinations

if __name__=='__main__':
    heights = [int(input()) for _ in range(9)]
    heights.sort()
    can = list(combinations(heights, 7))

    for c in can:
        if sum(c) == 100:
            for i in c:
                print(i)
            break
