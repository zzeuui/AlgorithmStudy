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
#실패한 경우
#문제 이해를 제대로 못 함. 비교를 하지 않은 다른 모든 노드들도 고려해야했는데
#비교한 정보만 있는 노드만을 위상정렬함
#75%에서 틀렸다고 채점됨
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
