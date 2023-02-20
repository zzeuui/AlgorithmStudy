
linked = [[0, 1, 2],
          [3, 7, 9, 11],
          [4, 10, 14, 15],
          [0, 4, 5, 6, 7],
          [6, 7, 8, 10, 12],
          [0, 2, 14, 15],
          [3, 14, 15],
          [4, 5, 7, 14, 15],
          [1, 2, 3, 4, 5],
          [3, 4, 5, 9, 13]]

class ClockSync():
    def __init__(self):
        self.min_cnt = 9999

    def push(self, clocks, switch):
        for l in linked[switch]:
            clocks[l] += 3
            if clocks[l] == 15: clocks[l] =3

    def solve(self, clocks, switch, cnt):

        if switch == len(linked): return 0

        for i in range(4):
            self.solve(clocks, switch+1, cnt)
            self.push(clocks, switch)
            cnt += 1
            
            if len(clocks)*12 == sum(clocks):
                if self.min_cnt > cnt: self.min_cnt = cnt
                return 1

if __name__=='__main__':
    case_n = input()

    for _ in range(int(case_n)):
        clocks = list(map(int, input().split(' ')))
        assert len(clocks) == 16, 'num of clocks must be 16'

        cs = ClockSync()

        switch = 0
        cnt = 0
        cs.solve(clocks, switch, cnt)
        if cs.min_cnt < 9999:
            print(cs.min_cnt)
        else:
            print(-1)

