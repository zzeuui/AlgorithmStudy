from collections import defaultdict
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

def dfs(here):
    global cnt
    visited[here] = cnt

    adj[here].sort()
    for i in adj[here]:
        if not visited[i]:
            cnt += 1
            dfs(i)

if __name__=='__main__':
    N, M, R = map(int, input().split())
    adj = defaultdict(list)
    visited = [0]*(N+1)

    for _ in range(M):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)

    cnt = 1
    dfs(R)

    for i in visited[1:]:
        print(i)
