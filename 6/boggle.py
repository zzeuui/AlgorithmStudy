import numpy as np

around_ind = [-6, -5, -4, 1, -1, 4, 5, 6]

#input
board = [['U','R','L','P','M'],
         ['X','P','R','E','T'],
         ['G','I','A','E','T'],
         ['X','T','N','Z','Y'],
         ['X','O','Q','R','S']]
board = sum(board, [])

"""
board = list()
for _ in range(25):
    board.append('A')
"""

word = list(input())

try:
    start_ind = board.index(word[0])
    start_inds = list()

    board_f = np.zeros(len(board))
    word_f = {w:0 for w in set(word)}
    start_f = np.zeros(len(board))

    def check_word(start_ind):

        start_f[start_ind] = 1

        if board[start_ind] in word:
            board_f[start_ind] = 1
            word_f[board[start_ind]] = 1

        for ai in around_ind:
            ni = start_ind + ai
            if ni >= 0 and ni <= len(board)-1:
                if board[ni] in word:
                    board_f[ni] = 1
                    word_f[board[ni]] = 1
                else:
                    board_f[ni] = -1

        start_inds = set(np.where(board_f > 0)[0])
        start_ind = list(start_inds - set(np.where(start_f > 0)[0]))
        if len(start_ind) > 0:
            start_ind = start_ind[0]
        else:
            return 1

        check_word(start_ind)

        if np.where(board_f == 0)[0].shape[0] == 0:
            return 1

    done = check_word(start_ind)

    print(len(word_f) == sum(word_f.values()))

except:
    print(False)

