import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

from collections import defaultdict

def dfs(here):

    if visited[here]:
        return

    visited[here] = True

    for i in adj[here]:
        if not visited[i]:
            dfs(i)

    order.append(here)

def forgotten(here):
    for i in par[here]:
        if not visited[i]:
            return True
    return False

if __name__ == '__main__':

    N, M = map(int, input().split())
    adj = defaultdict(list)
    par = defaultdict(list)
    visited = [0]*(N+1)
    order = list()

    for _ in range(M):
        a, b = map(int , input().split())
        adj[a].append(b)
        par[b].append(a)


    for i in range(1, N+1):
        if not visited[i] and not forgotten(i):
            dfs(i)

    print(' '.join([ str(o) for o in order[::-1]]))

"""
if __name__ == '__main__':

    N, M = map(int, input().split())
    adj = defaultdict(list)
    visited = [0]*(N+1)
    order = list()

    for _ in range(M):
        a, b = map(int , input().split())
        adj[a].append(b)

    for i in list(adj.keys()):
        if not visited[i]:
            dfs(i)

    print(' '.join([ str(o) for o in order[::-1]]))
"""
