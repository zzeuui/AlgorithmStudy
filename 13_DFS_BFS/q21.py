"""
정답 40분 (40분)

bfs로 연합 형성
"""
from collections import deque
import sys
input = sys.stdin.readline

def solution(n, l, r, A):

    direction = [(-1, 0),(1, 0),(0, -1),(0, 1)]

    day = -1

    while True:
        #하루
        day += 1
        group = 0
        visited = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):

                #하나의 연합
                if visited[i][j] == 0:

                    group += 1
                    total = 0
                    cnt = list()

                    q = deque()
                    q.append((i, j))
                    visited[i][j] = 1
                    total += A[i][j]
                    cnt.append((i, j))

                    while q:
                        x, y = q.popleft()
                        for dx, dy in direction:
                            nx, ny = x+dx, y+dy
                            # 인접 나라 접근
                            if nx >= 0 and nx < n and ny >= 0 and ny < n and visited[nx][ny] == 0:
                                # 차이 검사 
                                diff = abs(A[x][y] - A[nx][ny])
                                # 조건에 맞으면 연합에 포함
                                if diff >= l and diff <= r:
                                    q.append((nx, ny))
                                    visited[nx][ny] = 1
                                    total += A[nx][ny]
                                    cnt.append((nx, ny))

                    new_num = total // len(cnt)
                    for cx, cy in cnt:
                        A[cx][cy] = new_num

        # 연합의 수가 모든 나라 수와 같으면 중단, 연합 안 인구 이동x
        if group == n*n:
            break

    return day

if __name__=='__main__':
    n, l, r = map(int, input().split())

    A = list()
    for _ in range(n):
        A.append(list(map(int, input().split())))

    print(solution(n, l, r, A))
