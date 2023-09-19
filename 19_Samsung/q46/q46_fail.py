"""
오답 

책 풀이를 보면 논리 흐름이 동일한데,
*dist의 초기값이라던가, 먹을수있는 물고기를 설정할 때의 조건 순서가 다름*
이 부분 잘 확인해서 다시 풀어보기
"""

import sys
input = sys.stdin.readline
import copy
from collections import deque
import heapq

def calculate_distance(x, y):
    global n, shark_size

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    q = deque()
    q.append((x, y, 0))
    distance[x][y] = -2

    min_dist = float('inf')
    ret = list()

    while q:
        x, y, c = q.popleft()

        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < n and distance[nx][ny] == 0:
                q.append((nx, ny, c+1))
                distance[nx][ny] = c+1

                if 0 < graph[nx][ny] < shark_size: 
                    if c+1 < min_dist:
                        min_dist = c+1
                        heapq.heappush(ret, (nx, ny))

                    elif min_dist == c+1:
                        heapq.heappush(ret, (nx, ny))

    if not ret:
        return False
    else:
        return (ret[0], min_dist)

if __name__=='__main__':
    n = int(input())
    graph = list()
    for _ in range(n):
        graph.append(list(map(int, input().rstrip().split())))

    x, y = 0, 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 9:
                x, y = i, j
                
    shark_size = 2
    distance = copy.deepcopy(graph)

    time = 0
    cnt = 0
    while True:
        distance = [[-1 if shark_size < x < 9 else 0 for x in y] for y in graph]
        ret = calculate_distance(x, y)

        if not ret:
            break
        else:
            (x, y), c = ret
            cnt += 1

            graph[x][y] = 0
            
            time += c

        if cnt == shark_size:
            shark_size += 1
            cnt = 0

    print(time)
