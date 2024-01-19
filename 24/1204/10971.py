import sys
input = sys.stdin.readline

from itertools import permutations

def tsp(here, cost, visited):
    global n, ret

    if ret < cost:
        return

    if len(visited) == n and road[visited[-1]][visited[0]] != 0:
        ret = min(ret, cost+road[visited[-1]][visited[0]])

    for nt in range(n):
        if road[here][nt] != 0 and nt not in visited:
            visited.append(nt)
            tsp(nt, cost+road[here][nt], visited)
            visited.pop(-1)

if __name__=='__main__':
    n = int(input())
    road = [list(map(int, input().rstrip().split())) for _ in range(n)]

    ret = float('inf')
    for i in range(n):
        tsp(i, 0, [i])

    print(ret)
