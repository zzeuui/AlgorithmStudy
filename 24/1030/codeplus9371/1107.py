import sys
input = sys.stdin.readline

def solution(n, m, broken):
    
    # 1
    if n == 100:
        return 0

    # 2 +/-
    ret = abs(n-100)

    # 3
    if m == 0:
        ret = min(ret, len(str(n)))

    # 4
    worked = set([str(i) for i in range(10) if i not in broken])
    for i in range(1000000):
        num = list(str(i))
        if set(num) <= worked:
            ret = min(ret, len(num) + abs(n-i))
            
    return ret

if __name__=='__main__':
    n = int(input())
    m = int(input())
    broken = list()
    if m > 0:
        broken = list(map(int, input().rstrip().split()))

    print(solution(n, m, broken))
