import sys
input = sys.stdin.readline

def dfs(x, y, a):
    global n, m, k, ret

    if len(s) == k:
        ret = max(ret, a)
        return


    for x in range(x, n):
        for y in range(m):
            if [x, y] not in s:
                if ([x+1, y] not in s) and ([x-1, y] not in s) and ([x, y+1] not in s) and ([x, y-1] not in s):
                    s.append([x, y])
                    dfs(x, y, a+board[x][y])
                    s.pop()

if __name__=='__main__':
    n, m, k = map(int, input().rstrip().split())
    board = [list(map(int, input().rstrip().split())) for _ in range(n)]

    if k == 1:
        print(max(sum(board, [])))
    else:
        s = list()
        ret = float('-inf')
        visited = [[1]*m for _ in range(n)]
        dfs(0, 0, 0)
        print(ret)
