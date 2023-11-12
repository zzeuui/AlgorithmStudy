import sys
input = sys.stdin.readline

from itertools import combinations

if __name__=='__main__':
    l, c = map(int, input().rstrip().split())
    alphabets = input().rstrip().split()
    alphabets.sort()

    ess = set(['a', 'e', 'i', 'o', 'u'])
    for can in list(combinations(alphabets, l)):
        canset = set(can)
        if (not ess.isdisjoint(canset)) and (len(canset-ess) > 1):
            print(''.join(can))


