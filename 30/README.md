# 최단 경로 알고리즘

- 도입
   - 음수 간선
     - 가중치의 합이 음수인 사이클(음수 사이클)이 존재하는 그래프의 경우 최단 경로를 찾을 수 없음
   - 단일 시작점과 모든 쌍 알고리즘
     - 하나의 시작점에서 모든 정점으로 가는 최단 거리를 계산하는 단일 시작점 알고리즘을 정점 수 만큼 수행하여 모든 쌍 알고리즘을 구현할 수도 있지만, 목적에 맞는 효율적인 알고리즘이 각각 존재함
   - 방향 그래프와 무방향 그래프
     - 최단 거리 알고리즘은 방향 그래프 기준으로 동작
     - 무방향 그래프의 경우 두 정점 사이를 양방향으로 통행할 수 있도록 변환  
       *음수 가중치가 있는 무방향 그래프에 대해서는 알고리즘 적용 불가능

### 다익스트라(Dijkstra)의 최단 경로 알고리즘

- 우선순위 큐를 사용해 정점과 해당 정점까지의 최단 거리를 쌍으로 저장
- 우선순위 큐는 정점까지의 최단 거리를 기준으로 정점을 배열함, BFS와 비슷하게 거리를 기준으로 가까운 정점부터 검사
- 이미 저장된 해당 정점까지 가는 거리보다 크면 그 간선은 무시함
- 방문한 정점을 다시 방문하지 않는 다익스트라 알고리즘의 경우, 음수 간선이 있는 그래프에는 적용하지 못함

- 방문 여부 확인 없이 우선순위 큐로 구현
   ```
   #해당 코드는 방문한 정점을 다시 방문하기 때문에, 음수 사이클이 없다면 음수 간선이 있는 그래프에도 적용할 수 있음
   #그러나 정점 개수에 따라 시간 복잡도가 지수적으로 증가할 수 있음
   import heapq
   import collections

   #{'node1':[['node2', dist], ...] ...}
   graph = collections.defaultdict(list)

   def dijkstra(start):
      q = list()
      heapq.heappush(q, [0, start])
      distance[start] = 0

      while q:
      dist, now = heapq.heappop(q)

      //기존의 최단 거리보다 길면, 볼 필요도 없음
      if distance[now] < dist:
         continue

      for next_node, next_dist in graph[now]:
         cost = dist + next_dist
         if cost < distance[next_node]:
            distance[next_node] = cost
            heapq.heappush(q, [cost, next_node])

   ```
- 방문 여부 확인과 함께 우선순위 큐 없이 구현
   ```
   INF = int(le9)
   import collections

   #{'node1':[['node2', dist], ...] ...}
   graph = collections.defaultdict(list)
   visted = {k: False for k in list(graph.keys())}
   distance = {k: INF for k in list(graph.keys())}

   def get_smallest_node():
      min_v = INF
      index = 0
      for k in list(graph.keys()):
         if distance[k] < min_v and not visited[k]:
            min_v = distance[k]
            index = k
      return k, min_v

    def dijkstra(start):
      #시작 정점
      distance[start] = 0
      visited[start] = True

      #시작정점 인접한 정점에 대한 거리 갱신
      for next_node, next_dist in graph[start]:
         distance[next_node] = next_dist

      #시작 정점 이외의 다른 모든 노드 방문
      while True:
         now, min_v = get_smallest_node()

         #모든 정점을 방문해 min_v가 갱신되지 않았을 때 종료
         if min_v == INF: break

         visited[now] = True
         for next_node, next_dist in graph[now]:
            cost = distance[now] + next_dist
            if cost < distance[next_node]:
               distance[next_node] = cost
   ```
- 코드에 대한 자세한 설명: https://doing7.tistory.com/76 

### 벨만-포드(Bellman-Ford)의 최단 경로 알고리즘

- 정의 
    - 시작점에서 각 정점까지 가는 최단 거리의 상한을 예측하고 그 값을 배열에 저장. 예측값과 실제 최단 거리 사이의 오차를 반복적으로 줄여나가며, 최종적으로 배열에는 실제 최단 거리가 저장됨
    - 음수 간선이 있는 그래프에 적용할 수 있고 음수 사이클 존재여부 확인이 가능함

- 구현
    - 시작점 $s$가 존재할 때 $upper[s] = 0$, $upper[a] = inf$  $(a != s)$임
    - 또한 $(u, v)$ 경로에 대해서 $dist[v] <= dist[u] + w(u, v)$ 임  
      * $dist[a]$: $s$부터 $a$까지의 최단 거리
    - $upper[v]$는 최대 $dist[u]+w(u,v)$ 값을 가질 수 있으므로 해당 값으로 갱신함
    - 위와 같이 $upper[v]$를 갱신하며 감소하는 작업을 $(u,v)$에 따라 완화한다고 표현
    - 다음 과정을 |V|번 반복
      - 모든 간선을 하나씩 확인
      - 최단 거리 upper 갱신
      - V번 째에도 완화에 성공하면 음수 사이클이 존재함
    ```
    #g = {node1: [[node2, weight12], [node3, weight13]...], node2:...}
    g = collections.defaultdict(list)
    
    def bellmanFord(src):
      upper = [float('inf')]*V
      upper[src] = 0
      updated = False
      
      for _ in range(V):
         updated = False
         for here in range(V):
            for there, cost in g[here]:
               if upper[there] > upper[here]+cost:
                  upper[there] = upper[here]+cost
                  updated = True
        
         #모든 간선 완화 실패할 경우 종료         
         if not updated: break 
      
      #마지막 반복에서도 완화에 성공하면, 음수사이클이 존재함으로
      #빈 리스트 리턴
      if updated: upper = list()
      
      return upper
    ```
