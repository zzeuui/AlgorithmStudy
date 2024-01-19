import sys
input = sys.stdin.readline

from itertools import groupby

def count_board(board):
    global ret

    #row
    temp = list()
    for b in board:
        temp.extend([len(list(g)) for k, g in groupby(b)])

    ret = max(ret, max(temp))

    #colum
    board = sum(board, [])
    for i in range(n):
        b = board[i::n]
        temp.extend([len(list(g)) for k, g in groupby(b)])

    ret = max(ret, max(temp))

if __name__=='__main__':
    n = int(input())
    board = [list(input().rstrip()) for _ in range(n)]

    ret = 0
    count_board(board)

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for x in range(n):
        for y in range(n):
            for dx, dy in directions:
                nx, ny = x+dx, y+dy
                if 0 <= nx < n and 0 <= ny < n:
                    board[x][y], board[nx][ny] = board[nx][ny], board[x][y]
                    count_board(board)
                    board[x][y], board[nx][ny] = board[nx][ny], board[x][y]

    print(ret)
