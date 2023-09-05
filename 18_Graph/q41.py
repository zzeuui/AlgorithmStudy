"""
정답 20분(40분)

여행계획에 포함된 노드들이 같은 루트 노드를 가지는 지 확인
-> 같은 그래프에 속하는지 여부
"""
import sys
input = sys.stdin.readline

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
    n, m = map(int, input().rstrip().split())
    
    parent = [i for i in range(n)]

    graph = list()
    for a in range(n):
        for b, e in enumerate(list(map(int, input().rstrip().split()))):
            if e == 1:
                union_parent(parent, a, b)


    wants = list(map(int, input().rstrip().split()))
    wants = [e-1 for e in wants]

    flag = True
    std = parent[wants[0]]
    for i in wants[1:]:
        if std != parent[i]:
            flag = False
            break

    if flag:
        print("YES")
    else:
        print("NO")
