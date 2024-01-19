import sys
input = sys.stdin.readline
from itertools import groupby

def check_sequence(board):
    global n, ret

    #row
    temp = [len(list(g)) for b in board for r, g in groupby(b)]
    ret = max(ret, max(temp))

    #colum
    temp = list()
    for i in range(n):
        temp.extend([len(list(g)) for r, g in groupby(sum(board, [])[i::n])])

    ret = max(ret, max(temp))

if __name__=='__main__':
    n = int(input())
    board = [list(input().rstrip()) for _ in range(n)]

    ret = 0

    check_sequence(board)

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for x in range(n):
        for y in range(n):
            for dx, dy in directions:
                nx, ny = x+dx, y+dy
                if 0 <= nx < n and 0 <= ny < n:
                    board[x][y], board[nx][ny] = board[nx][ny], board[x][y]
                    check_sequence(board)
                    board[x][y], board[nx][ny] = board[nx][ny], board[x][y]

                if ret == n:
                    break
    print(ret)
