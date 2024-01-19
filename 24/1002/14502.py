import copy
import sys
input = sys.stdin.readline

DIRECTION = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def spread(x, y):
    global n, m

    lab[x][y] = 2

    for dx, dy in DIRECTION:
        nx, ny = x+dx, y+dy
        if 0 <= nx < n and 0 <= ny < m and lab[nx][ny] == 0:
            spread(nx, ny)

if __name__=='__main__':
    n, m = map(int, input().rstrip().split())
    lab = list()
    virus = list()
    empty = list()

    for i in range(n):
        lab.append(list(map(int, input().rstrip().split())))
        for j in range(m):
            if lab[i][j] == 2:
                virus.append((i, j))
            if lab[i][j] == 0:
                empty.append((i, j))
    
    ori_lab = copy.deepcopy(lab)

    n_empty = len(empty)
    cnt = -1
    for i in range(n_empty-2):
        for j in range(i+1, n_empty-1):
            for k in range(j+1, n_empty):

                lab = copy.deepcopy(ori_lab)

                for h in (i, j, k):
                    lab[empty[h][0]][empty[h][1]] = 1

                for x, y in virus:
                    spread(x, y)

                cnt = max(cnt, sum(lab, []).count(0))
    
    print(cnt)
