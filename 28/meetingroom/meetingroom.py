from itertools import combinations, chain
import sys
input = sys.stdin.readline

def disjoint(a, b):
    return a[1] <= b[0] or b[1] <= a[0]

vertex_counter = scc_counter = 0
def tarjanSCC(adj):
    scc_id = [-1]*len(adj)
    discovered = [-1]*len(adj)
    scc_counter = vertex_counter = 0
    st = []

    def scc(here):
        global vertex_counter, scc_counter
        vertex_counter += 1
        ret = discovered[here] = vertex_counter
        st.append(here)
        for i in range(len(adj[here])):
            there = adj[here][i]
            if discovered[there] == -1:
                ret = min(ret, scc(there))
            elif scc_id[there] == -1:
                ret = min(ret, discovered[there])
        if ret == discovered[here]:
            while True:
                t = st.pop()
                scc_id[t] = scc_counter
                if t == here:
                    break
            scc_counter += 1
        return ret

    for i in range(len(adj)):
        if discovered[i] == -1:
            scc(i)
    return scc_id


def solve2sat():
    n = len(adj) // 2
    label = tarjanSCC(adj)
    
    if any(a == b for a, b in zip(*[iter(label)]*2)):
        return False

    value = [-1]*(2*n)
    print(label)
    order = sorted((-label[i], i) for i in range(2*n))
    print(order)

    for i in range(2*n):
        vertex = order[i][1]
        variable = vertex // 2
        is_true = vertex % 2 == 0
        if value[variable] != -1:
            continue
        value[variable] = not is_true

    print(value)

    retur value


if __name__=='__main__':
    for C in range(int(input())):
        N = int(input())
        meetings = tuple(
            zip(*[chain(*(map(int, input().split()) for _ in range(N)))]*2))

        scc_counter = vertex_counter = 0

        # make graph
        adj = [[] for _ in range(4*N)]
        for i, j in ((a, a+1) for a in range(0, 2*N, 2)):
            adj[2*i+1].append(2*j)
            adj[2*j+1].append(2*i)
        for i, j in combinations(range(2*N), 2):
            if not disjoint(meetings[i], meetings[j]):
                adj[i*2].append(2*j+1)
                adj[j*2].append(2*i+1)

        ans = solve2sat()
        if ans:
            print('POSSIBLE')
            for i in range(N):
                if ans[2*i] == True:
                    print(meetings[2*i])
                else:
                    print(meetings[2*i+1])
        else:
            print('IMPOSSIBLE')
