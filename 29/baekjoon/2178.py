import sys
import collections

input=sys.stdin.readline

def bfs(start):
    distance = [-1 for _ in range(N*M)]
    
    q = list()

    distance[start] = 1
    q.append(start)

    while q:
        here = q.pop(0)

        for nt_node in g[here]:
            if distance[nt_node] == -1:
                distance[nt_node] = distance[here] + 1
                q.append(nt_node)

    return distance


if __name__=='__main__':
    N, M = map(int, input().split())

    adj = [-1, -M , M, 1]

    maze = list()
    for _ in range(N):
        maze.extend([c for c in input().rstrip()])

    g = collections.defaultdict(list)
    for i in range(N*M):
        if i%M == 0: ne_adj = adj[1:]
        elif i%M == M-1: ne_adj = adj[:-1]
        else: ne_adj = adj

        if maze[i] == '1':
            for a in ne_adj:
                try:
                    if maze[i+a] == '1' and i+a > 0: g[i].append(i+a)
                except:
                    continue

    discovered = bfs(0)
    print(discovered[-1])
