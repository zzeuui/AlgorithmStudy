import sys
import collections

input = sys.stdin.readline

def floyd():
    # 1: k, 2: i or j
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])

    return dist

if __name__=='__main__':
    n = int(input())
    m = int(input())

    dist = [[float('inf')]*(n) for _ in range(n)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        dist[a][a] = 0
        if dist[a][b] > c:
            dist[a][b] = c

    dist = floyd()

    for d in dist:
        print(' '.join([str(e) for e in d]).replace('inf', '0'))
