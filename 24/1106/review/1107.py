import sys
input = sys.stdin.readline

def solution(broken):
    global n, m
    
    if n == 100:
        return 0

    ret = abs(100-n)

    if m == 0:
        ret = min(ret, len(list(str(n))))

    worked = [str(i) for i in range(10) if i not in broken]
    for i in range(1000000):
        butn = list(str(i))

        if set(butn) <= set(worked):
            ret = min(ret, len(butn) + abs(i-n))

    return ret

if __name__=='__main__':
    n = int(input())
    m = int(input())
    if m == 0:
        broken = list()
    else:
        broken = list(map(int, input().rstrip().split()))

    print(solution(broken))


