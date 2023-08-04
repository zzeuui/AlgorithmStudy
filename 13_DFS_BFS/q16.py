"""
정답(1시간 50분)

나: 완전탐색으로 울타리 설치하고, BFS로 바이러스 퍼트림
책: DFS로 울타리 설치하고, DFS로 바이러스 퍼트림

논리흐름은 비슷한 것 같은데, 책이 코드가 더 이쁘다.
"""
import copy
from collections import deque
import sys
input = sys.stdin.readline

def spread_sim(n, m, lab):

    test = copy.deepcopy(lab)

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    visited = [[0]*m for _ in range(n)]
    q = deque()

    for x, y in virus:
        if visited[x][y] == 0:
            q.append((x, y))
            visited[x][y] = 1
            while q:
                x, y = q.popleft()
                for i, j in zip(dx, dy):
                    nx, ny = x+i, y+j
                    if nx >= 0 and nx < n and ny >= 0 and ny < m and visited[nx][ny] == 0 and test[nx][ny] != 1:
                        visited[nx][ny] = 1
                        test[nx][ny] = 2
                        q.append((nx, ny))

    cnt = 0
    for x in test:
        for y in x:
            if y == 0:
                cnt += 1
    return cnt

def check_empty(sme):
    for k in sme:
        x, y = empty[k]
        if lab[x][y] != 0:
            return False
    
    return True

n, m = map(int, input().rstrip().split())
lab = list()
empty = list()
virus = list()
for i in range(n):
    l = list(map(int, input().rstrip().split()))
    lab.append(l)
    for j in range(m):
        if l[j] == 0:
            empty.append((i, j))
        if l[j] == 2:
            virus.append((i, j))

ret = -1
for start in range(len(empty)-2):
    for mid in range(start+1, len(empty)-1):
        for end in range(mid+1, len(empty)):
            if check_empty([start, mid, end]): 
                init_lab = copy.deepcopy(lab)
                for k in [start, mid, end]:
                    x, y = empty[k]
                    lab[x][y] = 1

                ret = max(ret, spread_sim(n, m, lab))

                lab = init_lab

print(ret)
