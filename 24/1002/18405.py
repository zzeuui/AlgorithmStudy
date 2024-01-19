import sys
input = sys.stdin.readline

from collections import deque

DIRECTION = [(-1, 0), (1, 0), (0, -1), (0, 1)]
if __name__=='__main__':
    n, k = map(int, input().rstrip().split())
    virus = list()
    examiner = list()
    for i in range(n):
        examiner.append(list(map(int, input().rstrip().split())))
        for j in range(n):
            if examiner[i][j] != 0:
                virus.append((examiner[i][j], i, j))

    s, x, y = map(int, input().rstrip().split())
    x, y = x-1, y-1

    q = deque([(i, j, 0) for _, i, j in sorted(virus, key=lambda x:x[0])])

    while q:
        i, j, t = q.popleft()

        if t == s:
            break

        for di, dj in DIRECTION:
            ni, nj = i+di, j+dj
            if 0 <= ni < n and 0 <= nj < n and examiner[ni][nj] == 0:
                examiner[ni][nj] = examiner[i][j]
                q.append((ni, nj, t+1))

    print(examiner[x][y])
