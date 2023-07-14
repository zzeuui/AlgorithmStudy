# 09 최단 경로

## 1) 가장 빠른 길 찾기
- 최단 경로(Shortest Path) 알고리즘은 가장 짧은 경로를 찾는 알고리즘
- 보통 노드와 간선으로 표현된 그래프에서 경로를 찾는 문제임
- 일반적으로 코테에서는 최단 거리를 요구하기 때문에, 최단 경로를 다루지 않음

### 다익스트라(Dijkstra) 최단 경로 알고리즘
#### 개요
- 특정한 노드에서 출발해 다른 노드로 가는 각각의 최단 경로를 구해주는 알고리즘
- 그래프의 음의 간선이 없을 때 정상적으로 동작
- 매번 '가장 비용이 적은 노드'를 선택하는 과정을 반복하기 때문에 기본적으로 그리디 알고리즘으로 분류
- 과정
  - 출발 노드를 설정한다
  - 출발 노드와 연결된 간선으로 최단 거리 테이블을 초기화한다
  - 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택한다
    - 노드가 두 개 이상일 경우, 일반적으로 작은 번호 선택
    - 선택된 노드의 최단 거리는 감소하지 않음    
    $\Rightarrow$ 한 단계당 하나의 노드에 대한 최단 거리를 확실히 찾는 것으로 이해
  - 해당 노드를 거쳐 다른 노드로 가는 비용을 계산해 최단 거리 테이블을 갱신한다
  - 세번째와 네번째 과정을 반복한다

#### 방법 1. 간단한 다익스트라 알고리즘
- 구현하기 쉽지만 느리게 동작하는 코드
- 시간 복잡도 $O(V^2)$
  - $V$: 노드의 개수
- 단계마다 '방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택'하기 위해 매 단계마다 1차원 리스트(최단 거리 테이블)의 모든 원소를 확인(순차 탐색)
- 구현
```
def dijkstra(start):
  # 시작 노드에 대해서 초기화
  distance[start] = 0
  visited[start] = True
  for j in graph[start]:
    distance[j[0]] = j[1] #j:(노드, 간선 가중치)
  
  for i in range(n-1):
    now = get_smallest_node() # 방문하지 않은 노드 중, 최단 거리가 짧은 노드
    vistited[now] = True
    for j in graph[now]:
      cost = distance[now] + j[1]
      if cost < distance[j[0]]:
        distance[j[0]] = cost
```

#### 방법 2. 개선된 다익스트라 알고리즘 (외워야함)
- 구현하기에 조금 더 까다롭지만 빠르게 동작하는 코드
- 시간복잡도 $O(ElogV)$
  - $V$: 노드의 개수, $E$: 간선의 개수
- 최소 힙(Min Heap)으로 구현된 우선순위 큐를 사용해 출발 노드로부터 가장 거리가 짧은 노드를 빠르게 찾음
  - 우선순위 큐: 우선순위가 가장 높은 데이터를 가장 먼저 삭제
  - PriorityQueue보다는 heapq 라이브러리가 빠르게 동작하고 기본적으로 최소 힙을 기반으로 함
  - 원소로 튜플을 입력받으면 튜플의 첫번째 원소를 기준으로 우선순위 큐를 구성함
  - 최대 힙처럼 사용하려면 음수(-)를 붙여서 넣었다가, 꺼낸 다음에 다시 음수(-)를 붙여줌
- 구현
  - 현재 가장 가까운 노드를 저장하기 위한 목적으로만 우선순위 큐를 추가로 이용
```
import heapq

def dijkstra(start):
  q = list()
  #시작 노드로 가기 위한 최단 경로는 0으로 설정해, 큐에 삽입
  heapq.heappush(q, (0, strat))
  distance[start] = 0
  while q:
    dist, now = heapq.heappop(q)
    # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
    if distance[now] < dist:
      continue
    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))
```

### 플로이드 워셜(Floyd-Warshall) 알고리즘
#### 개요
- 모든 지점에서 다른 모든 지점까지의 최단 경로를 모두 구하는 알고리즘
- 시간 복잡도 $O(N^3)$
- 2차원 리스트에 최단 거리 정보를 저장
- $D_{ab} = min(D_{ab}, D_{ak} + D_{kb})$의 점화식을 기반으로 동작하는 다이나믹 프로그래밍 알고리즘으로 분류
  - A에서 B로 가는 비용($D_{ab}$)와 A에서 K를 거쳐 B로 가는 비용($D_{ak}+D_{kb})$ 중 더 작은 값으로 최단 거리를 갱신
- 과정
  - 연결된 간선 정보들에 따라 최단 거리 테이블 초기화
  - 연결되어 있지 않으면 무한대 값을 가지고, 자기 자신에 대해서는 0으로 초기화
  - 하나의 노드를 선택해, 해당 노드를 거쳐갔을 때의 거리를 기반으로 최단 거리 갱신
  - 모든 노드에 대해 세번째 과정을 수행 

#### 구현
```
# 그래프 표현을 만들고, 모든 값을 무한으로 초기화
graph = [[INF]*(V+1) for _ in range(V+1)]
#자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for i in range(V+1):
  graph[i][i] = 0
#각 간선 정보를 입력받아 그래프 초기화
for _ in range(E):
  a, b, c = map(int, input().split())
  graph[a][b] = c

# 점화식에 따라 프로이드 워셜 알고리즘 수행
for k in range(1, V+1):
  for a in range(1, V+1):
    for b in range(1, V+1):
      graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])
```

## 2) 미래 도시
- 문제
  - 1번부터 N번까지 노드가 주어졌을 때, 1번에서 K번을 거쳐 X번으로 가는 최단 거리 계산
  - 모든 간선의 가중치는 1이며, 양방향 이동 가능
  - X번에 도달할 수 없으면 -1 출력
- 풀이
  - 나: 다익스트라 두 번 수행함..
  ```
  from collections import defaultdict
  import heapq
  
  n, m = map(int, input().split())
  graph = defaultdict(list)
  for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
  x, k = map(int, input().split())
  def func(start):
    distance = [float('inf')]*(n+1)
    q = list()
    heapq.heappush(q, (0,start))
    while q:
      dist, now = heapq.heappop(q)
      if dist > distance[now]:
        continue
      for b in graph[now]:
        cost = dist+1
        if distance[b] > cost:
          distance[b] = cost
          heapq.heappush(q, (cost, b))

    return distance

  ret = func(1)[k] + func(k)[x]
  if ret == float('inf'):
    print(-1)
  else:
    print(ret)
  ```
  - 책: 플로이드 워셜 알고리즘 적용
  ```
  INF = int(1e9)
  n, m = map(int, input().split())
  graph = [[INF]*(n+1) for _ in range(n+1)]
  for i in range(n+1):
    graph[i][i] = 0
  for _ in range(m):
    graph[a][b] = 1
    graph[b][a] = 1
  x, k = map(int, input().split())

  for k in range(1, n+1):
    for a in range(1, n+1):
      for b in range(1, n+1)
        graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

  ret = graph[1][k] + graph[k][x]
  if ret >= INF:
    print(-1)
  else:
    print(ret)
  ```

## 3) 전보
- 문제
  - N개의 도시와 M개의 통로가 존재할 때, C도시에서 보내느 메시지를 받는 도시의 개수와 모두 메시지를 받는데 걸리는 시간
  - 가중치가 있는 방향 그래프
- 풀이
  - 다익스트라 알고리즘으로 풀이
  ```
  from collections import defaultdict
  import heapq

  n, m, c = map(int, input().split())
  graph = defaultdict(list)
  for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))
  
  def func(start):
    distance = [float('inf')]*(n+1)
    
    q = list()
    heapq.heappush(q, (0, start))

    while q:
      dist, now = heapq.heappop(q)
      if dist > distance[now]:
        continue
      for y, z in graph[now]:
        cost = dist+z
        if cost < distance[y]:
          distance[y] = cost
          heapq.heappush(q, (cost, y))

    return distance

  ret = [x for x in func(c) if x != float('inf')]
  print(len(ret), max(ret))
  ```
