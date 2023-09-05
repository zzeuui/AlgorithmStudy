"""
정답 19분 (40분)

최소 신장 트리: 크루스칼

활성화했을 때 최소 금액이 아닌,
*절약할 수 있는 최대 금액을 출력하기. 문제 제대로 읽기 몇 분 헤맴

"""
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
    n, m = map(int, input().split())

    parent = [i for i in range(n)]

    edges = list()
    total = 0
    for _ in range(m):
        x, y, z = map(int, input().split())
        edges.append((z, x, y))
        total += z
    edges.sort()
    
    result = 0
    for edge in edges:
        z, x, y = edge

        if find_parent(parent, x) != find_parent(parent, y):
            union_parent(parent, x, y)
            result += z


    print(total-result)
