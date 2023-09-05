"""
오답: 메모리 초과
"""
import sys
input = sys.stdin.readline

from collections import defaultdict

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])

    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

if __name__=='__main__':
    n = int(input())

    nodes = list()
    for _ in range(n):
        x, y, z = map(int, input().split())
        nodes.append((x, y, z))

    edges = list()
    for i in range(n):
        for j in range(i+1, n):
            node1 = nodes[i]
            node2 = nodes[j]

            cost = min(abs(node1[0]-node2[0]), abs(node1[1]-node2[1]), abs(node1[2]-node2[2]))

            edges.append((cost, i , j))

        nodes[i] = i

    edges.sort()

    result = 0
    for edge in edges:
        cost, a, b = edge
        if find_parent(nodes, a) != find_parent(nodes, b):
            union_parent(nodes, a, b)
            result += cost

    print(result)
