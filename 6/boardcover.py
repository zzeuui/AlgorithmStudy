import copy

class BoardCover():
    def __init__(self, h, w):
        self.h = h
        self.w = w
        self.total = h*w
        self.num = 0

        self.COVER_TYPE = [[1, self.w], [1, self.w+1], 
                           [self.w, self.w+1], [self.w, self.w-1]]

    def print_board(self, board):
        print('***************')

        for i, b in enumerate(board, start=1):
            print(b, end='')

            if i%(self.w) == 0 and i > 2:
                print()

    def cover(self, board):

        try:
            x = board.index(0)
        except:
            return 0

        board_temp = copy.deepcopy(board)
        for c_t in self.COVER_TYPE:
            set_f = False

            for t in c_t:
                ni = x+t
                if ni < 0 or ni > self.total-1:
                    set_f = False
                    break;
                elif board[ni]+1 > 1 or board[x]+1 > 1:
                    set_f = False
                    break;
                else:
                    set_f = True

            if set_f:
                board[x] = 1
                for t in c_t:
                    ni = x+t
                    board[ni] = 1

                if sum(board) == self.total:
                    self.num += 1
                    return 1
                else:
                    self.cover(board)
                    board = copy.deepcopy(board_temp)

        if board_temp == board:
            return 0

if __name__=='__main__':
    case_n = input()

    for _ in range(int(case_n)):
        h_w = input().split(' ')
        h = int(h_w[0])
        w = int(h_w[1])

        board = list()
        for _ in range(h):
            row = list(map(int, input().replace('#', '1').replace('.', '0')))
            assert len(row) == w, 'column is invalid'
            board.extend(row)

        if len(board)-sum(board)%3 == 0:
            bc = BoardCover(h, w)
            done = bc.cover(board)
            print(bc.num)
        else:
            print(0)

