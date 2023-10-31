import sys
input = sys.stdin.readline

def solution(n, m, broken):
    # n is 100
    if n == 100:
        return 0

    ret = float('inf')

    # no broken
    if len(broken) == 0:
        ret = len(list(str(n)))

    # + or -
    ret = min(ret, abs(n-100))
    
    # broken
    MAX = 1000000
    worked = set([str(x) for x in range(10) if x not in broken])
    for i in range(MAX+1):
        v = list(str(i))
        if set(v) <= worked:
            v = len(v)
            ret = min(ret, abs(n-i)+v)

    return ret

if __name__=='__main__':
    n = int(input())
    m = int(input())
    broken = list()
    if m > 0:
        broken = list(map(int, input().rstrip().split()))

    print(solution(n, m, broken))
