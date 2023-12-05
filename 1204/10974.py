import sys
input = sys.stdin.readline

from itertools import permutations

if __name__=='__main__':
    n = int(input())
    for p in list(permutations(range(1, n+1))):
        print(' '.join(list(map(str, p))))
