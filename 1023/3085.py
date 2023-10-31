
def check_board(board):
    global n, ret

    #row
    temp = list()
    for b in board:
        v = 1
        for i in range(n-1):
            if b[i] == b[i+1]:
                v += 1
            else:
                temp.append(v)
                v = 1
        temp.append(v)

    #colum
    board = sum(board, [])
    for i in range(n):
        v = 1
        b = board[i::n]
        for i in range(n-1):
            if b[i] == b[i+1]:
                v += 1
            else:
                temp.append(v)
                v = 1
        temp.append(v)

    ret = max(ret, max(temp))

def solution(board):
    global n, ret

    DIRECTION = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    check_board(board)

    for x in range(n):
        for y in range(n):
            for dx, dy in DIRECTION:
                nx, ny = x+dx, y+dy
                if 0 <= nx < n and 0 <= ny < n:
                    board[x][y], board[nx][ny] = board[nx][ny], board[x][y]
                    check_board(board)
                    if ret == n:
                        return

                    board[x][y], board[nx][ny] = board[nx][ny], board[x][y]


if __name__=='__main__':
    n = int(input())
    board = [list(input()) for _ in range(n)]

    ret = 0
    solution(board)
    print(ret)
