"""
(1,1)에서 (N, N)으로 이동하는 최단 거리를 계산하는 BFS문제

구현:
- 로봇 위치 이동, 회전에 대해 로봇이 차지한 두 위치 모두 계산.
- 주어진 맵에 외곽에 벽(1)으로 채워 로봇의 위치에 대한 범위 판정을 간단히 함.
- 집합에서 {(1, 1), (1, 2)}와 {(1, 2), (1, 1)}은 동일함. 집합 객체로 방문 여부 판단
"""

from collections import deque

# **모든 가능한 로봇의 두 위치 계산**
def get_next_pos(pos, board):
    next_pos = []
    pos = list(pos)
    pos1_x, pos1_y, pos2_x, pos2_y = pos[0][0], pos[0][1], pos[1][0], pos[1][1]
    # 상하좌우 처리
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        pos1_nx, pos1_ny = pos1_x+dx[i], pos1_y+dy[i]
        pos2_nx, pos2_ny = pos2_x+dx[i], pos2_y+dy[i]
        if board[pos1_nx][pos1_ny] == 0 and board[pos2_nx][pos2_ny] == 0:
            next_pos.append({(pos1_nx, pos1_ny),(pos2_nx, pos2_ny)})

    # 로봇이 가로로 놓여 있는 경우
    if pos1_x == pos2_x:
        for i in [-1, 1]:
            #위쪽 혹은 아래쪽 두 칸이 모두 비어 있다면
            if board[pos1_x + i][pos1_y] == 0 and board[pos2_x + i][pos2_y] == 0:
                next_pos.append({(pos1_x, pos1_y),(pos1_x+i, pos1_y)})
                next_pos.append({(pos2_x, pos2_y),(pos2_x+i, pos2_y)})

    # 로봇이 세로로 놓여 있는 경우
    if pos1_y == pos2_y:
        for i in [-1, 1]:
            # 왼쪽 혹은 오른쪽 두 칸이 모두 비어 있다면
            if board[pos1_x][pos1_y+i] == 0 and board[pos2_x][pos2_y+i] == 0:
                next_pos.append({(pos1_x, pos1_y),(pos1_x, pos1_y+i)})
                next_pos.append({(pos2_x, pos2_y),(pos2_x, pos2_y+i)})

    #현재 위치에서 이동할 수 있는 위치를 반환
    return next_pos

def solution(board):
    n = len(board)
    new_board = [[1]*(n+2) for in range(n+2)] #**외곽에 벽(1)을 추가해 범위 판정 단순화
    for i in range(n):
        for j in range(n):
            new_board[i][j] = board[i][j]

    q = deque()
    visited = []
    pos = {(1, 1), (1, 2)}
    q.append((pos, 0))
    visited.append(pos) #**집합 객체로 방문 처리**

    while q:
        pos, cost = q.popleft()
        if (n, n) in pos:
            return cost

        for next_pos in get_next_pos(pos, new_board):
            if next_pos not in visited: #**집합 객체로 방문 처리
                q.append((next_pos, cost+1))
                visited.append(next_pos)

    return 0
