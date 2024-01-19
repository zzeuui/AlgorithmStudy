import sys
input = sys.stdin.readline

from bisect import bisect_left

if __name__=='__main__':
    n = int(input())
    soldiers = list(map(int, input().rstrip().split()))[::-1]

    ret = [soldiers[0]]

    for s in soldiers[1:]:
        r = ret[-1]

        if r < s:
            ret.append(s)
        else:
            ind = bisect_left(ret, s)
            ret[ind] = s

    print(n-len(ret))
