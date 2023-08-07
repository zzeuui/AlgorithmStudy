"""
정답 1시간 30분 (60분)

dfs(재귀호출)로 선생님의 상하좌우 각 방향에 대해 학생이 있는지 검사 
"""

import sys
sys.setrecursionlimit(10**7)

def dfs(x, y, dx, dy):
    global n, space
    
    if x >= 0 and x < n and y >= 0 and y < n:
        if space[x][y] == 'S':
            return False
        elif space[x][y] ==  1:
            return
        else:
            return dfs(x+dx, y+dy, dx, dy)

def check_space(teacher):
    global n

    direction = [(-1, 0),(1, 0),(0, -1),(0, 1)]

    visited = [[0]*n for _ in range(n)]
    for tx, ty in teacher:
        for dx, dy in direction:
            if dfs(tx, ty, dx, dy) == False:
                return False

    return True

def solution(n, space):

    teacher = list()
    empty = list()
    for i in range(n):
        for j in range(n):
            if space[i][j] == 'T':
                teacher.append((i, j))
            elif space[i][j] == 'X':
                empty.append((i, j))

    for i, o1 in enumerate(empty[:-2]):
        j = i + 1
        for o2 in empty[j:-1]:
            j += 1
            for o3 in empty[j:]:
                space[o1[0]][o1[1]] = 1
                space[o2[0]][o2[1]] = 1
                space[o3[0]][o3[1]] = 1
                if check_space(teacher) is not False:
                    return "YES"
                space[o1[0]][o1[1]] = 0
                space[o2[0]][o2[1]] = 0
                space[o3[0]][o3[1]] = 0

    return "NO"

if __name__=='__main__':
    n = int(input())
    space = list()
    for i in range(n):
        space.append(input().split())

    print(solution(n, space))
