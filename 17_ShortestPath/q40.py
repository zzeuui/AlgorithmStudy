"""
정답 15분(40분)
"""
import heapq
from collections import Counter

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
distance = [float('inf')]*n

for _ in range(m):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

q = list()
heapq.heappush(q, (0, 0))
distance[0] = 0

while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
        continue

    for nt in graph[now]:
        cost = dist+1
        if cost < distance[nt]:
            distance[nt] = cost
            heapq.heappush(q, (cost, nt))

dist = max(distance)
ind = distance.index(dist) + 1
cnt = Counter(distance)[dist]

print(ind, dist, cnt)
