"""
55분
뱀이 이동하고 벽에 부딪혔을 때 게임 종료되는 것까지는 구현했는데,
자기 몸에 부딪혔을 때 종료되는 알고리즘은 구현 못 함
어떻게 구현해야할 지 감도 안 잡힘
"""

n = int(input())
board = [[0]*n for _ in range(n)]

k = int(input())
for _ in range(k):
    x, y = map(int, input().split())
    board[x-1][y-1] = 1 

l = int(input())
move = list()
for _ in range(l):
    xc = input().split()
    xc[1] = 0 if xc[1] == 'L' else 1
    move.append((int(xc[0]), xc[1]))

ret = 1

length = 1
x, y = 0, 0

direction = 3 # 0:up, 1:down, 2:left, 3:right
direction_table = [[2, 3], # up -> L / D
                   [3, 2], # down -> L / D
                   [1, 0],    # left -> L / D
                   [0, 1]]    # right -> L / D
done = False

while True:
    if done:
        break

    time, action = move.pop(0)
    for _ in range(time):

        if direction == 0: x -= 1
        elif direction == 1: x += 1
        elif direction == 2: y -= 1
        elif direction == 3: y += 1

        if x >= n or x < 0 or y >= n or y < 0:
            done = True
            break
        else:
            ret += 1
            if board[x][y] == 1:
                length += 1
                
    direction = direction_table[direction][action]

print(ret)
