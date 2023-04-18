import sys
import collections

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

def scc(here):
    global th, sccCnt
    discovered[here] = th
    th += 1
    stack.append(here)

    parent = discovered[here]

    for next_node in G[here]:
        if discovered[next_node] == -1: 
            parent = min(parent, scc(next_node))
        elif on_stack[next_node] == -1: 
            parent = min(parent, discovered[next_node])
        else:
            indegree[on_stack[next_node]] += 1

    if parent == discovered[here]:
        while True:
            t = stack.pop()
            on_stack[t] = sccCnt
            if t == here:
                break

        if stack:
            indegree[sccCnt] += 1

        sccCnt += 1

    return parent

if __name__=='__main__':

    for _ in range(int(input())):
        inline = input()
        if inline == '\n':
            continue

        V, E = map(int, inline.split())
        G = collections.defaultdict(list)

        for _ in range(E):
           u, v = map(int, input().rstrip().split())
           G[u].append(v)

        discovered = [-1]*V
        on_stack = [-1]*V
        stack = list()
        th = sccCnt = 0

        indegree = [0]*V

        for i in range(V):
            if discovered[i] == -1:
                scc(i)

        #on_stack = [abs(s-sccCnt+1) for s in on_stack]

        """
        for i in range(V):
            for node in G[i]:
                if on_stack[i] != on_stack[node]:
                    indegree[on_stack[node]] += 1
        """

        cnt = 0
        for i in range(sccCnt):
            if indegree[i] == 0:
                check = i
                cnt += 1

        if cnt == 1:
            for r in range(V):
                if check == on_stack[r]:
                    print(r)
        else:
            print("Confused")

        print()
