import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
nums = list(map(int, input().rstrip().split()))
nums.sort()

s = list()

def dfs():
    for l in range(len(s)-1):
        if s[l] > s[l+1]:
            return

    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for i in nums:
        s.append(i)
        dfs()
        s.pop()

dfs()
