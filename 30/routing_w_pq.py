import sys
import collections
import heapq

input = sys.stdin.readline

def dijkstra(start):
    q = list()
    heapq.heappush(q, [1.0, start])
    distance[start] = 1.0

    while q:
        dist, now = heapq.heappop(q)

        for next_node, next_distance in g[now]:
            cost = dist * next_distance
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(q, [cost, next_node])

if __name__=='__main__':
    for _ in range(int(input())):
        n, m = map(int, input().rstrip().split())

        g = collections.defaultdict(list)
        distance = [1e9]*n

        for _ in range(m):
            a, b, c = map(float, input().rstrip().split())

            g[int(a)].append((int(b), c))
            g[int(b)].append((int(a), c))

        dijkstra(0)
        print(distance[-1])
