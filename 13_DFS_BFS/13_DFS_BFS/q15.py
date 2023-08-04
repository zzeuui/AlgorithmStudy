"""
26분

** list로 구현해서 시간초과 계속됨. deque로 구현하기**
** input은 sys.stdin.readline으로**
"""
from collections import defaultdict, deque
import sys
input = sys.stdin.readline

n, m, k, x= map(int, input().rstrip().split())
g = defaultdict(list) 
for _ in range(m):
    a, b = map(int, input().rstrip().split())
    g[a].append(b)

dis = [n]*(n+1)
vis = [0]*(n+1)

q = deque()
q.append(x)
vis[x] = 1
dis[x] = 0

while q:
    now = q.popleft()
    for nt in g[now]:
        if not vis[nt]:
            vis[nt] = 1
            dis[nt] = min(dis[nt], dis[now]+1)
            q.append(nt)

flag = False
for i, d in enumerate(dis):
    if d == k:
        flag = True
        print(i)

if not flag:
    print(-1)
