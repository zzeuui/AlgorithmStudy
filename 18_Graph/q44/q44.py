"""
책 풀이

모든 간선을 고려하게되면, 내가 했던 것처럼 N(N-1)/2가 됨.
   
그런데, 거리가 min(|x1 - x2|, |y1 - y2|, |z1 - z2|)로 계산됨으로,
x축, y축, z축으로 각각 정렬을 수행하고 각 축에 대한 간선을 독립적으로 다룰 수 있음
즉, 3*(N-1)개의 간선 비용을 계산하여 크루스칼 알고리즘 수행
"""

def find_parent():
    ...

def union_parent():
    ...

def main():
    ...

    x = []
    y = []
    z = []

    for i in range(1, n+1):
        data = list(map(int, input().split()))
        x.append((data[0], i))
        y.append((data[1], i))
        z.append((data[2], i))

    x.sort()
    y.sort()
    z.sort()

    for i in range(n-1):
        #cost, a, b
        edges.append((x[i+1][0] - x[i][0], x[i][1], x[i+1][1]))
        edges.append((y[i+1][0] - y[i][0], y[i][1], y[i+1][1]))
        edges.append((z[i+1][0] - z[i][0], z[i][1], z[i+1][1]))

    edges.sort()

    ...


