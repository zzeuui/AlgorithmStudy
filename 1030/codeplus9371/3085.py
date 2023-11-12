import sys
input = sys.stdin.readline

def check_board(board):
    global n

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

    board = sum(board, [])
    for i in range(n):
        b = board[i::n]
        v = 1
        for i in range(n-1):
            if b[i] == b[i+1]:
                v += 1
            else:
                temp.append(v)
                v = 1
        temp.append(v)

    return max(temp)

def solution(board):
    global n

    DIRECTION = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    ret = check_board(board)
    if ret == n:
        return n

    for x in range(n):
        for y in range(n):
            for dx, dy in DIRECTION:
                nx, ny = x+dx, y+dy
                if 0 <= nx < n and 0 <= ny < n:
                    board[x][y], board[nx][ny] = board[nx][ny], board[x][y]
                    ret = max(ret, check_board(board))
                    board[x][y], board[nx][ny] = board[nx][ny], board[x][y]

                    if ret == n:
                        return n

    return ret

if __name__=='__main__':
    n = int(input())
    board = [list(input().rstrip()) for _ in range(n)]
    
    print(solution(board))
