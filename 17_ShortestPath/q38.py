"""
오답

책 풀이:
    A에서 B로 도달이 가능하거나, B에서 A로 도달이 가능하면 '성적 비교'가 가능
    플로이드 워셜 알고리즘 수행 후, 모든 노드에 대하여 다른 노드와 서로 도달이 가능한지를 체크
"""
import sys
input = sys.stdin.readline

INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    graph[i][i] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

result = 0
#각 학생을 번호에 따라 한 명씩 확인하며 도달 가능한지 체크
for i in range(1, n+1):
    cnt = 0
    for j in range(1, n+1):
        if graph[i][j] != INF or graph[j][i] != INF:
            cnt += 1
    if cnt == n:
        result += 1

print(result)
