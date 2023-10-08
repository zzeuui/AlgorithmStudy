import sys
input = sys.stdin.readline
import copy

DIRECTION = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def search(x, y, dx, dy):
    global n

    if 0 <= x < n and 0 <= y < n: 
        if hall[x][y] == 'S':
            return False
        elif hall[x][y] == 'O':
            return True

        return search(x+dx, y+dy, dx, dy)

    return True

def monitor():
    ret = True
    for i, j in teachers:
        for dx, dy in DIRECTION:
            ret = ret and search(i, j, dx, dy)

    return ret

if __name__=='__main__':
    n = int(input())

    hall = list()
    teachers = list()
    empty = list()
    for i in range(n):
        hall.append(list(input().rstrip().split()))
        for j in range(n):
            if hall[i][j] == 'T':
                teachers.append((i, j))
            elif hall[i][j] == 'X':
                empty.append((i, j))

    ori_hall = copy.deepcopy(hall)

    n_empty = len(empty)
    flag = False
    for i in range(n_empty-2):
        for j in range(i+1, n_empty-1):
            for k in range(j+1, n_empty):
                hall = copy.deepcopy(ori_hall)

                for e in (i, j, k):
                    hall[empty[e][0]][empty[e][1]] = 'O'

                if monitor():
                    flag = True
                    break

    if flag:
        print('YES')
    else:
        print('NO')
