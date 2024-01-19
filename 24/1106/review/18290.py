import sys
input = sys.stdin.readline

def dfs(x, y, a):
    global v, k

    if len(ret) == k:
        v = max(v, a)
        return

    for x in range(x, n):
        for y in range(m):
            if [x, y] not in ret:
                if ([x+1, y] not in ret) and ([x-1, y] not in ret) and ([x, y+1] not in ret) and ([x, y-1] not in ret):
                    ret.append([x, y])
                    dfs(x, y, a+board[x][y])
                    ret.pop()

if __name__=='__main__':
    n, m, k = map(int, input().rstrip().split())
    board = [list(map(int, input().rstrip().split())) for _ in range(n)]

    if k == 1:
        print(max(sum(board, [])))
    else:
        ret = list()
        v = float('-inf')
        dfs(0, 0, 0)
        print(v)
