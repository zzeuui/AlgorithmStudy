import sys
import collections
import heapq

input = sys.stdin.readline

def dijkstra(start):
    q = list()
    heapq.heappush(q, [0, start])
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        for next_node, next_distance in g[now]:
            cost = dist + next_distance
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(q, [cost, next_node])

if __name__=='__main__':
    for _ in range(int(input())):
        V, E, n, m = map(int, input().split())
        g = collections.defaultdict(list)
        distance = [float('inf')]*(V+1)

        for _ in range(E):
            a, b, t = map(int, input().split())

            g[a].append((b, t))
            g[b].append((a, t))

        fire = list(map(int, input().split()))
        house = list(map(int, input().split()))

        #this part
        for h in house:
            g[0].append((h, 0))
            g[h].append((0, 0))

        dijkstra(0)

        time = 0
        for i in fire:
            time += distance[i]
        print(time)
