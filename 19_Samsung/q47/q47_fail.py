"""
문제 정리

1. 상어는 (0,0) 물고기를 먹고, (0,0) 물고기의 방향과 상향의 방향은 동일함
2. 물고기의 이동
  2-1. 번호가 작은 물고기부터,
  2-2. 빈칸과 다른 물고기가 있는 칸 가능, 상어와 공간을 벗어나는 곳 불가능
  2-3. 이동할 수 있는 칸을 찾을 때까지 반시계(왼쪽)으로 45도 회전
  2-4. 이동할 수 없으면 이동하지 않음. 이동가능하면 한칸 이동
  2-5. 다른 물고기가 있으면 서로 위치를 바꿈

3. 상어의 이동
  3-1. 먹은 물고기의 방향을 가짐
  3-2. 한 번에 여러칸 지나갈 수 있고, 지나간 칸의 물고기는 먹지 않음
  3-3. 물고기가 없는 칸으로 이동할 수 없음

=> 출력: 상어가 먹을 수 있는 물고기 번호의 합의 최댓값.

DFS + 완탐?
BFS + 완탐?

=> 한 번 의사결정이 될 때마다 환경이 달라지기때문에, 재귀호출을 사용하는 DFS가 맞을 듯
+입력이 작아서 재귀호출+완탐 가능할 것 같음
"""

def print_board(board):
    for b in board:
        print(' '.join([str(e) for e in b]))

import sys
input = sys.stdin.readline

N = 4

DIRECTIONS = {1: (-1, 0), 2: (-1, -1),
              3: (0, -1), 4: (1, -1),
              5: (1, 0),  6: (1, 1),
              7: (0, 1),  8: (-1, 1)}

def move_fish(graph, fish, shark):
    s_x, s_y = shark[2], shark[3]

    for f in fish:
        x, y = f[2], f[3]
        d = f[1]
        nx, ny = x, y

        while True:
            dx, dy = DIRECTIONS[d]
            nx, ny = x+dx, y+dy

            if (nx != s_x or ny != s_y) and 0 <= nx < N and 0 <= ny < N:
                nf = graph[nx][ny]
                nf = [nf[0], nf[1], x, y]
                f = [f[0], f[1], nx, ny]
                graph[x][y] = nf
                graph[nx][ny] = f

                for i in range(len(fish)):
                    if fish[i][0] == nf[0]:
                        break

                fish[i] = graph[x][y]
                break

            d = (d+1)%8
            if d == 0:
                d += 1

    return graph, fish

def dfs(x, y, shark, vistied, graph, fish):
    global ret
    
    #현재까지의 탐색의 결과 값을 판단
    if shark[0]+graph[x][y][0] > ret:
        ret = shark[0]+graph[x][y][0]

    #상어 상태
    shark = [shark[0]+graph[x][y][0], #지금까지의 물고기 합
             graph[x][y][1],          #상어 방향
             x, y]                    #x, y = graph[x][y][2], graph[x][y][3]

    #DFS 방문 표시
    #visited[graph[x][y][2]][graph[x][y][3]] = 1
    visited[x][y] = 1
    fish = [f for f in fish if f[0] != graph[x][y][0]]

    #물고기 이동
    graph, fish = move_fish(graph, fish, shark)

    #상어의 이동, DFS
    """
    - 현재 방향으로 가까운 물고기부터 먼 물고기까지의 선택(즉, 최대 세 가지 경우)
    - 상어는 회전하지 않음
    - x:다음 x위치, y:다음 y위치, shark: 현재 상어 상태, 같이 들어간 graph에 따라 다음 상태로..
    - visitied, graph, fish: 상어가 현재 위치하고, 물고기가 이동한 후의 환경
    - 이미 방문한 위치는 물고기가 없어 이동할 수 없음
    """
    #현재 상어의 방향으로
    dx, dy = DIRECTIONS[shark[1]]
    #최대 N-1번 이동 가능(맵 제한 조건 N*N)
    for i in range(N-1):
        x, y = x+dx, y+dy

        if 0 <= x < N and 0 <= y < N:
            #이미 방문해서 물고기가 없으면 더 이상 그 방향으로 이동할 수 없음
            if visited[x][y] == 1:
                break
            else:
                dfs(x, y, shark, visited, graph, fish)

if __name__=='__main__':
    graph = list()
    for i in range(N):
        g = list(map(int, input().rstrip().split()))
        g = [[g[j], g[j+1], i, j//2] for j in range(N*2)[::2]]
        graph.append(g)

    fish = sum(graph, [])
    fish = sorted(fish, key=lambda x:x[0]) 

    #[지금까지 합, 방향, x, y]
    shark = [0, 0, 0, 0]
    visited = [[0]*(N) for _ in range(N)]
    ret = 0

    #시작점이 (0, 0)으로 고정된 DFS
    dfs(0, 0, shark, visited, graph, fish)

    print(ret)
