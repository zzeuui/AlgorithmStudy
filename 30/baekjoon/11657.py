import sys
import collections

input = sys.stdin.readline

def bellamford(src):
    upper = [float('inf') for _ in range(N+1)]
    upper[src] = 0

    for _ in range(1, N+1):
        updated = False
        for here in range(1, N+1):
            for there, cost in g[here]:
                if upper[there] > upper[here]+cost:
                    upper[there] = upper[here]+cost
                    updated = True
        if not updated: break

    if updated: upper = list()

    return upper

if __name__=='__main__':
    N, M = map(int, input().split())

    g = collections.defaultdict(list)
    for _ in range(M):
        a, b, c = map(int, input().split())
        g[a].append((b, c))

    upper = bellamford(1)

    if not upper: print(-1)
    else:
        for i in upper[2:]:
            if i == float('inf'): print(-1)
            else: print(i)
