"""
정답 12분(40분)
"""
import sys
input = sys.stdin.readline

if __name__=='__main__':
    n = int(input())
    m = int(input())

    graph = [[float('inf')]*(n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        graph[i][i] = 0

    for _ in range(m):
        a, b, c = map(int, input().rstrip().split())
        graph[a][b] = min(graph[a][b], c)

    for k in range(1, n+1):
        for a in range(1, n+1):
            for b in range(1, n+1):
                graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

    for i, l in enumerate(graph):
        l = [x if x != float('inf') else 0 for x in l]
        graph[i] = l

    for l in graph[1:]:
        s = ' '.join([str(x) for x in l[1:]])
        print(s)
