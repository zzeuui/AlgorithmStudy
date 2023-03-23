# -*- coding: utf-8 -*- 

"""
처음에 문제만 봤을 때, 무향 그래프의 절단점 찾고 컴포넌트 수 구하기인 줄 알았음

그런데 풀이를 보면 주어진 문제의 그래프는 "루트 없는 트리"임
"한 번 지나간 갤러리를 다시 지나기 위해서는 전에 지난 복도를 반드시 지나야 한다"
루트 없는 트리의 속성
    1. 정확히 (정점수-1)개의 간선이 있음
    2. 사이클이 존재하지 않음
    3. 두 정점 사이를 연결하는 단순 경로가 정확히 하나 있음

그리고 "지배 집합 찾기"라는 유명한 문제임
각 정점이 자기 자신과 모든 인접한 정점들을 지배한다고 했을 때, 그래프의 모든 정점을 지배하는 정점의 부분집합을 그래프의 지배 집합이라고 함

==> 그러므로 이 문제는 루트 없는 트리 그래프에서 최소 지배 집합 수를 찾으면 됨
"""

import sys
input = sys.stdin.readline

def dfs(here):
    visited[here] = True
    children = [0, 0, 0]
    for there in adj[here]:
        if not visited[there]:
            #dfs(there)은 자식의 상태를
            #0(unwathced), 1(watched), 2(installed)로 반환
            children[dfs(there)] += 1

    #자식이 감시 중이 아니면 현재 노드에 카메라 설치
    if children[UNWATCHED]:
        global installed 
        installed += 1
        return INSTALLED
    
    #자식노드에 이미 카메라가 설치되어 있으면,
    #현재 노드에 카메라 설치할 필요 없음
    if children[INSTALLED]:
        return WATCHED

    #자식이 없거나, 이미 자식이 감시 중이면,
    #현재 노드에는 카메라를 설치하지 않고 부모 노드에게 감시 중이 아님을 반환
    return UNWATCHED

for _ in range(int(input())):
    V, E = map(int, input().split())
    #adj = [[]]*V 랑 visited = [False]*V하면 시간초과됨
    adj = [[] for _ in range(V)]
    visited = [False for _ in range(V)]
    UNWATCHED = 0
    WATCHED = 1
    INSTALLED = 2
    installed = 0

    for _ in range(E):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)

    for u in range (V):
        if not visited[u] and dfs(u) == UNWATCHED:
            #현재 노드 u가 감시 중이 아니라는 조건이기 때문에,
            #dfs(u)가 종료된 후 u를 감시하기 위해 설치함
            installed += 1

    print(installed)
