import sys
import collections

input = sys.stdin.readline

def bellmanFord():
    for _ in range(V):
        for here in range(V):
            for there, cost in g[here]:
                upper[there] = min(upper[there], upper[here]+cost)
                lower[there] = max(lower[there], lower[here]+cost)

if __name__=='__main__':
    
    for _ in range(int(input())):
        V, w = map(int, input().rstrip().split())
        
        g = collections.defaultdict(list)
        for _ in range(w):
            a, b, d = map(int, input().rstrip().split())
            g[a].append([b, d])

        src = 0

        upper = [float('inf') for _ in range(V)]
        upper[src] = 0
        lower = [float('-inf') for _ in range(V)]
        lower[src] = 0

        bellmanFord()
        ret1, ret2 = upper[1], lower[1]
    
        bellmanFord()
        if ret1 != upper[1]: ret1 = "INFINITY"
        if ret2 != lower[1]: ret2 = "INFINITY"
        if ret1 == float('inf') or ret2 == float('-inf'):
            print("UNREACHABLE")
        else:
            print(ret1, ret2)
