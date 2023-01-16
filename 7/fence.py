
class Fence():
    def __init__(self):
        self.highest = 0

    def compute(self, high):
        if len(high) == 1:
            return high[0]

        mid = int(len(high)/2) #7 --> 3
        left = 0
        right = len(high)

        left_sq = self.compute(high[left:mid])
        right_sq = self.compute(high[mid:right])

        l = high.index(max(high))
        r = l+1

        mid_est = len(high[l:r])*min(high[l:r])
        self.highest = max(self.highest, mid_est)

        while l-1 >= left and r+1 < right:
            if high[l-1] > high[r+1]:
                l -= 1
            else:
                r += 1

            mid_est = len(high[l:r])*min(high[l:r])
            self.highest = max(self.highest, mid_est)
            
            if mid_est < self.highest:
                break;

        self.highest = max(self.highest, left_sq, right_sq)

        return len(high)*min(high)

if __name__=='__main__':
    case_n = input()

    for _ in range(int(case_n)):
        n = input()
        high = list(map(int, input().split(' ')))

        f = Fence()
        f.compute(high)

        print(f.highest)
