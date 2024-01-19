import sys
input = sys.stdin.readline

def possible(idx):
    s = 0
    for i in range(idx, -1, -1):
        s += v[i]
        if S[i][idx] == 1 and s <= 0:
            return False
        if S[i][idx] == 0 and s != 0:
            return False
        if S[i][idx] == -1 and s >= 0:
            return False
    return True


def solve(idx):
    if idx == n:
        print(' '.join(map(str, v)))
        exit(0)

    if S[idx][idx] == 0:
        v[idx] = 0
        return solve(idx+1)

    for i in range(1, 11):
        v[idx] = i * S[idx][idx]
        if possible(idx):
            solve(idx+1)
        v[idx] = 0

if __name__=='__main__':
    n = int(input())
    arr = list(input())
    S = [[0]*n for _ in range(n)]

    v = [0]*n
    for i in range(n):
        for j in range(i, n):
            temp = arr.pop(0)
            if temp == '+':
                S[i][j] = 1
            elif temp == '-':
                S[i][j] = -1

    solve(0)
