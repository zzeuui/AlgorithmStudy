"""
구현 문제
"""
import sys
input = sys.stdin.readline
NUM_TO_DIR = {'1': (-1, 0), '2': (1, 0), '3':(0, -1), '4': (0, 1)}

def decide_direction(dx, dy):
    if dy == 0:
        if dx == -1:
            return 1
        else:
            return 2
    else:
        if dy == -1:
            return 3
        else:
            return 4

def move_shark(shark, graph, k):
    global m, n

    for i in range(1, m+1):
        if shark[i] == [-1]:
            continue

        x, y = shark[i][0], shark[i][1]
        directions = pri_tbl[i][shark[i][2]]
        move = False
        for dx, dy in directions:
            nx, ny = x+dx, y +dy
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == [0, 0]:
                    graph[nx][ny] = [i, k]
                    d = decide_direction(dx, dy)
                    shark[i] = [nx, ny, d]
                    move = True
                    break
                else:
                    if graph[nx][ny][0] < i:
                        shark[i] = [-1]
                        move = True
                        break

        if not move:
            for dx, dy in directions:
                nx, ny = x+dx, y +dy
                if 0 <= nx < n and 0 <= ny < n:
                    if graph[nx][ny][0] == i:
                        graph[nx][ny] = [i, k]
                        d = decide_direction(dx, dy)
                        shark[i] = [nx, ny, d]
                        break


    return shark, graph

def clean_graph(graph, std):
    global n

    for i in range(n):
        for j in range(n):
            if graph[i][j][1] == std:
                graph[i][j] = [0, 0]

    return graph

if __name__=='__main__':
    n, m, k = map(int, input().rstrip().split())

    shark = [[-1] for _ in range(m+1)]

    graph = list()
    for i in range(n):
        line = list(map(int, input().rstrip().split()))
        graph.append(line)
        for j in range(n):
            if line[j] > 0:
                shark[line[j]] = [i, j]
                graph[i][j] = [line[j], k]
            else:
                graph[i][j] = [0, 0]

    init_dir = list(map(int, input().rstrip().split()))
    for i in range(1, m+1):
        shark[i].append(init_dir[i-1])

    pri_tbl = [[-1]]
    for i in range(1, m+1):
        pri_tbl.append([-1])
        for _ in range(4):
            pri_tbl[i].append([NUM_TO_DIR[p] for p in input().rstrip().split()])

    for g in graph:
        print(g)

    #move_shark
    std = k
    clean = False
    for i in range(1, 5):
        k -= 1
        if k == 0:
            k = 4
            std -= 1
            if std == 0:
                std = k

        sahrk, graph = move_shark(shark, graph, k)

        print(i, 'movee')
        for g in graph:
            print(g)
        print(shark)
