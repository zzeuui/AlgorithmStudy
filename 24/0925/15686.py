import sys
input = sys.stdin.readline

from itertools import combinations

if __name__=='__main__':
    n, m = map(int, input().rstrip().split())
    chicken = list()
    house = list()

    for i in range(n):
        l = list(map(int, input().rstrip().split()))
        for j, e in enumerate(l):
            if e == 1:
                house.append((i, j))
            if e == 2:
                chicken.append((i, j))

    dis = [[0]*len(house) for _ in range(len(chicken))]
    for i, (cr, cc) in enumerate(chicken):
        for j, (hr, hc) in enumerate(house):
            dis[i][j] = abs(cr-hr) + abs(cc-hc)

    dis_com = combinations(dis, m)

    cost = float('inf')
    for com in dis_com:
        cur_cost = 0
        for j in range(len(house)):
            d = float('inf')
            for i in range(m):
                d = min(d, com[i][j])
            cur_cost += d

        cost = min(cur_cost, cost)

    print(cost)
