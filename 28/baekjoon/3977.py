# -*- coding: utf-8 -*-

import sys
import collections

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

def scc(here):
    discovered[here] = 1
    parent = cur = discovered[here]

    stack.append(here)

    for next_node in G[here]:
       if discovered[next_node] == -1: 
           parent = min(cur, scc(next_node))
       elif on_stack[next_node] == -1: 
           parent = min(cur, discovered[next_node])

    if parent == cur:
       while True:
           t = stack.pop()
           on_stack[t] = 1
           if t == here:
               break

    return parent

if __name__=='__main__':

    for _ in range(int(input())):
        u = input().rstrip().split()
        if len(u) > 0:
            V, E = map(int, u)
            G = collections.defaultdict(list)

            for _ in range(E):
               u, v = map(int, input().rstrip().split())
               G[u].append(v)

            stack = list()
            ans = list()

            for i in range(V):
                discovered = [-1]*V
                on_stack = [-1]*V
                if discovered[i] == -1:
                    scc(i)

                if V == sum(discovered):
                    ans.append(i)

            if ans:
                for i in ans:
                    print(i)
            else:
                print("Confused")

            print("")

