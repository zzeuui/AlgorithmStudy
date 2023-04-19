# -*- coding: utf-8 -*- 

import sys
import collections

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

def scc(here):
    global th, scc_cnt
    parent = discovered[here] = th
    th += 1
    st.append(here)

    for next_node in G[here]:
        if discovered[next_node] == -1:
            parent = min(parent, scc(next_node))
        elif on_st[next_node] == -1:
            parent = min(parent, discovered[next_node])

    if parent == discovered[here]:
        while True:
            t = st.pop()
            on_st[t] = scc_cnt
            if t == here:
                break
        scc_cnt += 1

    return parent

def solve2sat():
    global N

    for i in range(1, N+1):
        if on_st[-i] == on_st[i]:
            return False

    return True

if __name__=='__main__':

    N, M = map(int, input().rstrip().split())
    G = collections.defaultdict(list)

    """
    #처음에 이렇게 생각했는데 틀렸음
    for i in range(1, N+1):
        G[i].append(-i)
        G[-i].append(i)

    for _ in range(M):
        u, v = map(int, input().rstrip().split())
        G[u].append(v)
        G[v].append(u)
    """

    for i in range(1, N+1):
        G[i] = list()
        G[-i] = list()

    for _ in range(M):
        u, v = map(int, input().rstrip().split())
        G[-u].append(v)
        G[-v].append(u)

    ks = list(G.keys())
    discovered = {k: -1 for k in ks}
    on_st = {k: -1 for k in ks}
    st = list()
    th = scc_cnt = 0

    for i in ks:
        if discovered[i] == -1:
            scc(i)

    if solve2sat():
        print(1)
    else:
        print(0)

