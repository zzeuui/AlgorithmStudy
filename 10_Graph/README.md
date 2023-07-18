# 10 그래프 이론

## 1) 다양한 그래프 알고리즘
- 그래프란 노드(Node)와 노드 사이에 연결된 간선(Edge)의 정보를 가지고 있는 자료구조이다
- 문제에 '서로 다른 개체(혹은 객체)가 연결되어 있다'는 내용이 있으면 그래프 알고리즘을 연상해야함
  - EX) '여러 개의 도시가 연결되어 있다'
- 트리는 루트노드, 부모 노드, 자식 노드로 구성된 그래프의 일종
- 그래프는 인접 행렬과 인접 리스트로 구현될 수 있고, 문제에 따라 메모리와 시간을 염두하여 선택한다.
  - 인접행렬: 빠르게 원소에 접근
  - 인접리스트: 메모리 절약

### 서로소 집합(Disjoint Sets)
- 서로소 집합이란 공통 원소가 없는 두 집합을 의미함
  - {1, 2}와 {3, 4}는 서로소 관계. {1, 2}와 {2, 3}은 서로소 관계가 아님

#### 서로소 집합 자료구조
- 서로소 집합 자료구조란 서로소 부분 집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료구조임. union과 find 연산으로 조작함
  - union 합집합: 2개의 원소가 포함된 집합을 하나의 집합으로 합치는 연산
  - find 찾기: 특정한 원소가 속한 집합이 어떤 집합인지 알려주는 연산
- 서로소 집합 계산 알고리즘
  - union 연산을 확인하여, 서로 연결된 두 노드 A, B를 확인한다.
    - A와 B의 루트 노드 A\`와 B\`를 각각 찾는다.(재귀적으로 부모를 거슬러 올라감)
    - A\`를 B\`의 부모 노드로 설정한다 (A\` < B\`)
  - 모든 union 연산을 처리할 때까지 위 과정을 반복한다.
- 기본적인 서로소 집합 알고리즘 구현
  - 시간복잡도가 $O(VM)$으로 모든 원소가 같은 집합이라면 비효율적일 수 있음
    - $V$는 노드의 개수, $M$은 연산의 개수
```
def find_parent(parent, x):
  #루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
  if parent[x] != x:
    return find_parent(parent, parent[x])
  return x

def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

v, e = map(int, input().split())
# 부모를 자기 자신으로 초기화
parent = [0]*(v+1)
for i in range(1, v+1):
  parent[i] = i

# union 연산 수행
for _ in range(e):
  a, b = map(int, input().split())
  union_parent(parent, a, b)
```
- 경로 압축 기법 구현
  - find 함수를 간단한 과정으로 최적화. 부모 테이블 값을 루트로 갱신한다. 
```
def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x] 
```
#### 서로소 집합을 활용한 사이클 판별
- 서로소 집합은 무방향 그래프 내에서 사이클을 판별할 때 사용할 수 있음
  - 방향 그래프의 사이클 여부는 DFS로 판별 가능
- 과정
  - 각 간선을 확인하며 두 노드의 루트 노드를 확인한다
    - 루트 노드가 서로 다르다면 두 노드에 대해서 union 연산 수행
    - 루트 노드가 같다면 사이클이 발생한 것
  - 그래프에 포함된 모든 간선에 대해 위 과정을 반복
- 구현
```
cycle = False

for i in range(e):
  a, b = map(int, input().split())
  if find_parent(parent, a) == find_parent(parent, b):
    cycle = True
    break
  else:
    union_parent(parent, a, b)
```

### 신장 트리(Spanning Tree)
- 신장 트리는 하나의 그래프가 있을 때 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프이다. 하나의 그래프에서 여러 개의 신장 트리를 생성할 수 있음

#### 크루스칼 알고리즘(Kruskal Algorithm)
- 크루스칼 알고리즘은 최소 비용으로 만들 수 있는 신장 트리를 찾는 알고리즘이다. 모든 간선 중 가장 거리가 짧은 간선부터 집합에 포함시키며 그리디 알고리즘으로 분류됨.
- 과정
  - 간선 데이터를 비용에 따라 오름차순으로 정렬
  - 간선을 하나씩 확인하며 현재의 간선이 사이클을 발생시키는 지 확인
    - 사이클이 발생하지 않으면 최소 신장 트리에 포함
    - 사이클이 발생하면 해당 간선은 제외
  - 모든 간선에 대해 위 과정을 반복
- 구현
```
edges = []
result = 0

for _ in range(e):
  a, b, cost = map(int, input().split())
  edges.append((cost, a, b))

#간선을 비용순으로 정렬
edges.sort()

for edge in edges:
  cost, a, b = edge
  if find_parent(a) != find_parent(b):
    union_parent(parent, a, b)
    result += cost

print(result)
```

### 위상 정렬(Topology Sort)
- 위상 정렬은 방향 그래프의 모든 노드를 방향성에 거스르지 않도록 순서대로 나열하는 것이다. 
- 과정
  - 진입차수가 0인 노드를 큐에 삽입. 진입차수는 노드에 들어오는 간선 개수를 의미
  - 큐가 빌 때까지 다음의 과정을 반복
    - 큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 그래프에서 제거
    - 새로게 진입차수가 0이 된 노드를 큐에 삽입
- 모든 원소를 방문하기 전에 큐가 비면 사이클이 존재하는 것임
- 구현
```
from collections import deque

v, e = map(int, input().split())
indegree = [0]*(v+1)
graph = [[] for i in range(v+1)]

for _ in range(e):
  a, b = map(int, input().split())
  graph[a].append(b) #정점 A에서 B로 이동 가능
  indegree[b] += 1

#위상 정렬
def topology_sort():
  result = []
  q = deque()

  for i in range(1, v+1):
    if indegree[i] == 1:
      q.append(i)

  while q:
    now = q.popleft()
    result.append(now)
    for i in graph[now]:
      indegree[i] -= 1
      if indegree[i] == 0:
        q.append(i)
```

## 2) 팀 결성
- 문제
  - 0번부터 N번의 학생이 존재하고, M개의 연산이 주어졌을때 해당 연산을 수행
  - "0, a, b" 연산은 a와 b번 학생을 같은 팀으로 합치는 연산. "1, a, b"는 a와 b번 학생이 같은 팀인지 확인하고 같은 팀이라면 "YES"를 출력 아니라면 "NO"를 출력하는 연산.
- 풀이
  - 서로소 집합 알고리즘으로 풀이(~~8분~~)
```
def find_parent(x):
  if parent[x] != x:
    parent[x] = find_parent(parent[x])
  return parent[x]

def union_parent(a, b):
  x = find_parent(a)
  y = find_parent(b)
  if x < y:
    parent[y] = x
  else:
    parent[x] = y

n, m = map(int, input().split())
parent = [0]*(n+1)
for i in range(n+1):
  parent[i] = i
for _ in range(m):
  o, a, b = map(int, input().split())
  if not o:
    union_parent(a, b)
  else:
    if find_parent(a) == find_parent(b):
      print("YES")
    else:
      print("NO")
```

## 3) 도시 분할 계획
- 문제
  - N개의 집과 M개의 길이 존재할 때, 최소의 유지비용이 드는 길로 마을 구성한 뒤 마을을 두 개로 분리.
  - 두 개의 마을로 분리된 뒤 유지비용 출력
- 풀이
  - 크루스칼 알고리즘으로 최소 신장 트리를 구한 뒤 가장 비용이 큰 간선을 제거하여 마을을 두 개로 분리(~~18분~~)
```
n, m = map(int, input().split())
parent = [0]*(n+1)
for i in range(1, n+1):
  parent[i] = i

edges = list()
ret = 0

for _ in range(m):
  a, b, c = map(int, input().split())
  edges.append((c, a, b))

edges.sort()

for e in edges:
  c, a, b = e
  if find_parent(a) != find_parent(b):
    union_parent(a, b)
    ret += c 
    last_c = c

print(ret-last_c)
```

## 4) 커리큘럼
- 문제
  - 1번부터 N번까지 강의가 존재하고, 각각의 강의에 대한 강의 시간과 선수 강의 정보가 주어진다.
  - 정보를 바탕으로 N개의 강의에 대해 수강하기까지 걸리는 최소 시간을 각각 출력
- 풀이
  - 위상정렬 응용. 진입 차수가 0인 인접노드를 확인하면서 시간도 갱신해준다.
```
from collections import defaultdict
import heapq

def topology_sort():
  q = list()
  
  for i, deg in enumerate(indegree):
    if i != 0 and deg == 0:
      heapq.heappush(q, (-1*times[i], i))

  while q:
    _, now = heapq.heappop(q)
    for nt_node in graph[now]:
      indegree[nt_node] -= 1
      if indegree[nt_node] == 0:
        heapq.heappush(q, (-1*times[nt_node], nt_node))
        ret[nt_node] = ret[now]+times[nt_node]
  
  return ret

n = int(input())
graph = defaultdict(list)
indegree, times, ret = [0]*(n+1), [0]*(n+1), [0]*(n+1)

for i in range(1, n+1):
  info = list(map(int, input().split()))[:-1]
  times[i], ret[i] = info[0], info[0]
  for p in info[1:]:
    graph[p].append(i)

  indegree[i] = len(info[1:])

for t in topology_sort():
  print(t)
```
