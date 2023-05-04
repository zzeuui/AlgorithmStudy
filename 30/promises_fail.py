import sys

input = sys.stdin.readline

def floyd():
    for i, k, c in edges:
        for j in range(V):
            if dist[i][j] > dist[i][k]+dist[k][j]:
                dist[i][j] = dist[i][k]+dist[k][j]

def update(a, b, c):


if __name__=='__main__':
    for _ in range(int(input())):
        V, M, N = map(int, input().split())
        edges = list()
        for _ in range(M):
            a, b, c = map(int, input().split())
            edges.append((a,b,c))
            edges.append((b,a,c))

        dist = [[float('inf')]*V for _ in range(V)]

        for a, b, c in edges:
            dist[a][a] = 0
            dist[a][b] = c

        floyd()

        useless = 0
        for _ in range(N):
            a, b, c = map(int, input().split())
            if not update(a, b, c): useless += 1

        print(useless)


