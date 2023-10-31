import sys
input = sys.stdin.readline

def i_tetromino(n, m, board):
    # I tetromino
    #row
    temp = list()
    for b in board:
        v = sum(b[:4])
        temp.append(v)
        for i in range(m-4):
            v = v - b[i] + b[i+4]
            temp.append(v)

    #colum
    board = sum(board, [])
    for i in range(m):
        b = board[i::m]
        v = sum(b[:4])
        temp.append(v)
        for i in range(n-4):
            v = v - b[i] + b[i+4]
            temp.append(v)

    return max(temp)
    
def o_tetromino(n, m, board):
    board = sum(board, [])
    temp = list()
    for x in range(n-1):
        dp = [0]*m
        for y in range(m):
            j = y+(m*x)
            dp[y] = sum(board[j:m+j+1:m])

        for i in range(m-1):
            temp.append(dp[i] + dp[i+1])

    return max(temp)

def j_t_tetromino(n, m, board):

    temp = list()

    # 1
    for x, b in enumerate(board[:-1]):
        for y in range(m-2):
            bar = sum(b[y:y+3])
            temp.append(bar + board[x+1][y])
            temp.append(bar + board[x+1][y+2])
            temp.append(bar + board[x+1][y+1])

    # 2
    board = board[::-1]
    for x, b in enumerate(board[:-1]):
        for y in range(m-2):
            bar = sum(b[y:y+3])
            temp.append(bar + board[x+1][y])
            temp.append(bar + board[x+1][y+2])
            temp.append(bar + board[x+1][y+1])

    # 3
    board = board[::-1]
    board = sum(board, [])
    for x in range(n-2):
        for y in range(m-1):
            j = y+(m*x)
            bar = sum(board[j:(m*3)+j:m])
            temp.append(bar + board[j+1])
            temp.append(bar + board[(m*2)+j+1])
            temp.append(bar + board[m+j+1])

    # 4
    board = board[::-1]
    for x in range(n-2):
        for y in range(m-1):
            j = y+(m*x)
            bar = sum(board[j:(m*3)+j:m])
            temp.append(bar + board[j+1])
            temp.append(bar + board[(m*2)+j+1])
            temp.append(bar + board[m+j+1])
    
    return max(temp)

def z_tetromino(n, m, board):
    temp = list()

    # 1
    for x in range(1, n-1):
        for y in range(m-1):
            temp.append(sum(board[x][y:y+2])+board[x-1][y]+board[x+1][y+1])
            temp.append(sum(board[x][y:y+2])+board[x-1][y+1]+board[x+1][y])

    # 2
    board = sum(board, [])
    for x in range(n-1):
        for y in range(m-2):
            j = y+(m*x)
            temp.append(sum(board[j+1:m+j+2:m])+board[j]+board[m+j+2])
            temp.append(sum(board[j+1:m+j+2:m])+board[j+2]+board[m+j])

    return max(temp)


if __name__=='__main__':

    n, m = map(int, input().rstrip().split())
    board = [list(map(int, input().rstrip().split())) for _ in range(n)]

    # I tetromino
    ret = i_tetromino(n, m, board)
    # O tetromino
    ret = max(ret, o_tetromino(n, m, board))
    # J and T tetromino
    ret = max(ret, j_t_tetromino(n, m, board))
    # Z tetromino
    ret = max(ret, z_tetromino(n, m, board))
    # T tetromino

    print(ret)
