import sys
import collections

input=sys.stdin.readline

def bfs(start):
    discovered = [0 for _ in range(N+1)]
    q = list()

    t = 1
    q.append(start)

    while q:
        here = q.pop(0)
        discovered[here] = t
        t += 1

        for next_node in sorted(g[here]):
            if discovered[next_node] == 0:
                discovered[next_node] = -1
                q.append(next_node)

    return discovered

if __name__=='__main__':
    N, M, R = map(int, input().split())
    g = collections.defaultdict(list)
    for _ in range(M):
        u, v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)
    
    discovered = bfs(R)
    
    for i in discovered[1:]: print(i)
