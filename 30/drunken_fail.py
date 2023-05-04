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

