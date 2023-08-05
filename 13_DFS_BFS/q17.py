"""
정답 (25분)

나: 시간을 따로 빼서 계산
책: q에 해당하는 시간도 넣고, 이제 bfs에서 q의 s를 pop했을 때 target보다 크면 break

while q:
    virus, s, x, y = q.popleft()
    if s == target_s:
        break

    #주변 위치 확인
    for i in range(4):
    ...
        q.append((virus, s+1, nx, ny))

"""
from collections import deque
import heapq
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
data = list()
virus = list()
for i in range(n):
    info = list(map(int, input().split()))
    data.append(info)
    for j in range(n):
        if info[j] != 0:
            heapq.heappush(virus, (info[j], i, j))

s, x, y = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()
visited = [[0]*n for _ in range(n)]
while virus:
    v, i, j = heapq.heappop(virus)
    q.append((v, i, j))
    visited[i][j] = 1

one_iter = len(q)
nt_iter = 0
while q and s > 0:
    v, i, j = q.popleft()
    one_iter -= 1
    for a, b in zip(dx, dy):
        ni, nj = i+a, j+b
        if ni >= 0 and ni < n and nj >= 0 and nj < n and visited[ni][nj] == 0:
            visited[ni][nj] = 1
            data[ni][nj] = v
            q.append((v, ni, nj))
            nt_iter += 1

    if one_iter == 0:
        s -= 1
        one_iter = nt_iter

print(data[x-1][y-1])

