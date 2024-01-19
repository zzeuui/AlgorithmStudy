import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

s = []
nums = []
def dfs():

    for l in range(len(s)-1):
        if s[l] > s[l+1]:
            return

    if len(s) == m:
        ret = sorted(s)
        if ret not in nums:
            nums.append(ret)
            print(' '.join(map(str, ret)))
        return

    for i in range(1, n+1):
        s.append(i)
        dfs()
        s.pop()

dfs()
