import sys
import collections

input = sys.stdin.readline

def get_smallest_node():
    min_v = float('inf')
    index = 0
    for i in range(len(g)):
        if distance[i] < min_v and not visited[i]:
            min_v = distance[i]
            index = i

    return index, min_v

if __name__=='__main__':

    for _ in range(int(input())):
        n, m = map(int, input().split())
        g = collections.defaultdict(list)
        distance = [float('inf')]*n
        visited = [False]*n

        for _ in range(m):
            a, b, c = map(float, input().split())
            g[int(a)].append((int(b), c))
            g[int(b)].append((int(a), c))

        start = 0
        distance[start] = 1.0
        visited[start] = True

        for nx_node, nx_dist in g[start]:
            distance[nx_node] = nx_dist

        while True:
            now, min_v = get_smallest_node()

            if min_v == float('inf'): break

            visited[now] = True
            for nx_node, nx_dist in g[now]:
                cost = distance[now] * nx_dist
                if cost < distance[nx_node]:
                    distance[nx_node] = cost

        print(distance[-1])
        


