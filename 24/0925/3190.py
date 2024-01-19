import sys
input = sys.stdin.readline

DIRECTION = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def change_direction(dir_idx, c):
    if dir_idx == 0:
        if c == 'D': return 3
        else: return 2

    elif dir_idx == 1:
        if c == 'D': return 2
        else: return 3

    elif dir_idx == 2:
        if c == 'D': return 0
        else: return 1

    else:
        if c == 'D': return 1
        else: return 0

def check_over(snake, nt):
    global n

    if 0 < nt[0] <= n and 0 < nt[1] <= n and nt not in snake:
        return False
    else:
        return True
def print_snake(snake):
    global n
    board = [[0]*(n) for _ in range(n)]
    for s in snake:
        board[s[0]-1][s[1]-1] = 1

    print('snake')
    for b in board:
        print(b)

if __name__=='__main__':
    n = int(input())

    k = int(input())
    apple = [list(map(int, input().rstrip().split())) for _ in range(k)]

    l = int(input())
    changes = dict()
    for _ in range(l):
        t_d = input().rstrip().split()
        changes[int(t_d[0])] = t_d[1]

    snake = [[1, 1]]
    dir_idx = 3
    cur_dir = DIRECTION[dir_idx]
    time = 0

    while True:
        time += 1

        nt = [snake[-1][0] + cur_dir[0], snake[-1][1] + cur_dir[1]]

        if check_over(snake, nt):
            break

        snake.append(nt)

        if nt not in apple:
            snake.pop(0)
        else:
            apple.pop(apple.index(nt))

        #print_snake(snake)

        if time in changes.keys():
            dir_idx = change_direction(dir_idx, changes[time])
            cur_dir = DIRECTION[dir_idx]

    print(time)
