"""
플로이드 알고리즘:
    아무 정점도 경유하지 않는 최단 거리에서 시작해
    경유할 수 있는 정점을 하나씩 추가해가며 최단 거리 갱신

==> 단속에 시간이 적게 걸리는 정점부터 경유점으로 추가
"""

import sys
import collections

input = sys.stdin.readline

def floyd():
    dist = [[float('inf')]*(V+1) for _ in range(V+1)]
    w = [[float('inf')]*(V+1) for _ in range(V+1)]
    
    for a, b, c in edges:
        dist[a][a], w[a][a] = 0, 0
        dist[a][b], w[a][b] = c, c

    for k, t in T:
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
                w[i][j] = min(dist[i][j]+t, w[i][j])

    return w

if __name__=='__main__':
    V, E = map(int, input().rstrip().split())
    T = [0] + map(int, input().split())
    T = [[i, n] for i, n in enumerate(T)]
    T.sort(key=lambda x: x[1])
    edges = list()
    for _ in range(E):
        a, b, c = map(int, input().split())
        edges.append((a, b, c))
        edges.append((b, a, c))

    w = floyd()

    for _ in range(int(input())):
        u, v = map(int, input().split())
        print(w[u][v])

