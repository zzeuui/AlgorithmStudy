import sys
input = sys.stdin.readline

def dfs():
    global n, m

    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in range(1, n+1):
        s.append(i)
        dfs()
        s.pop()

if __name__=='__main__':
    n, m = map(int, input().rstrip().split())
    s = []

    dfs()
