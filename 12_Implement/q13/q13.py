# 30분
from itertools import combinations

n, m = map(int, input().split())
city = list()
chicken = list()
house = list()

for i in range(n):
    line = list(map(int, input().split()))
    city.append(line)
    for j in range(n):
        if city[i][j] == 1:
            house.append((i,j))
        elif city[i][j] == 2:
            chicken.append((i,j))

chicken_candi = combinations(chicken, m)
ret = float('inf')
for chic_can in chicken_candi:
    distance = [n*2]*len(house)
    for i, h in enumerate(house):
        r1, c1 = h
        for c in chic_can:
            r2, c2 = c
            distance[i] = min(distance[i], (abs(r1-r2)+abs(c1-c2)))
    ret = min(ret, sum(distance))

print(ret)
