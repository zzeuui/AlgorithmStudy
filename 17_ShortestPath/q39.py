"""
정답 14분(40분)
"""
import heapq

for _ in range(int(input())):
    n = int(input())
    graph = list()
    for _ in range(n):
        graph.append(list(map(int, input().split())))

    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    q = list()
    heapq.heappush(q, (graph[0][0], 0, 0))

    distance = [[float('inf')]*(n) for _ in range(n)]
    distance[0][0] = graph[0][0]

    while q:
        dist, a, b = heapq.heappop(q)
        if distance[a][b] < dist:
            continue
        
        for dx, dy in direction:
            nx, ny = a+dx, b+dy
            if 0 <= nx < n and 0 <= ny < n:
                cost = dist+graph[nx][ny]
                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(q, (cost, nx, ny))

    print(distance[n-1][n-1])
