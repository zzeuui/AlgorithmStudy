import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
nums = sorted(map(int, input().rstrip().split()))

s = []
ret = []
def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for i in nums:
        if i not in s:
            s.append(i)
            dfs()
            s.pop()

dfs()
