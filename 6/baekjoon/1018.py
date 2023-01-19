import copy

def print_board(n, board):
    print('***************')
    for i, b in enumerate(board, start=1):
        if b == -1:
            b = 'W'
        else:
            b = 'B'
        print(b, end='')
        if i%(n) == 0 and i > 2: print()

def re_draw(paint, board):
    draw = 0
    for i, e in enumerate(board):
        if e != paint:
            draw += 1

        #print(f'i: {i}, e: {e}, paint: {paint}, draw: {draw}')
        paint *= -1
        if (i+1)% 8 == 0:
            #print('row')
            paint *= -1

    return draw

if __name__=='__main__':
    n_m = list(map(int, input().split(' ')))
    n = n_m[0]
    m = n_m[1]

    CROP = sorted([m*i+j for j in range(8) for i in range(8)])

    board = list()

    for _ in range(n):
        board.extend(list(map(int, input().replace('W', '0').replace('B', '2'))))
    board = [e-1 for e in board]

    #print_board(n, board)

    diff = n*m
    indexs = list()
    cnt = 0
    min_draw = 8*8
    while True:
        board_temp = [board[c] for c in CROP]
        draw = min(re_draw(1, board_temp), re_draw(-1, board_temp))
        if min_draw > draw:
            min_draw = draw
            min_board = copy.deepcopy(board_temp)

        cnt += 1
        if m-cnt == 7:
            cnt = 0
            CROP = [c+8 for c in CROP]
        else:
            CROP = [c+1 for c in CROP]

        if CROP[-1] > n*m-1:
            break

    print(min_draw)
    #print_board(8, min_board)
    #re_draw(-1, min_board)
