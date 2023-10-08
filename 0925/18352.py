import sys
input = sys.stdin.readline

from collections import deque

if __name__=='__main__':
    n, m, k, x = map(int, input().rstrip().split())
    edges = [[] for _ in range(n+1)]

    for _ in range(m):
        a, b = map(int, input().rstrip().split())
        edges[a].append(b)

    q = deque()
    distance = {i: float('inf') for i in range(n+1)}

    q.append([0, x])
    distance[x] = 0

    while q:
        dis, now = q.popleft()

        if dis > distance[now]:
            continue

        for nt in edges[now]:
            cost = dis+1
            if cost < distance[nt]:
                distance[nt] = cost
                q.append([cost, nt])

    candit = [i for i, v in distance.items() if v == k]
    if candit:
        for c in candit:
            print(c)
    else:
        print(-1)
