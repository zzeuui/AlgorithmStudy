# 그래프의 너비 우선 탐색(Breadth First Search, BFS)

- 시작점에서 가까운 정점부터 순서대로 방문하는 탐색 알고리즘. 두 정점 사이의 간선 수가 적을수록 가까운 정점으로 정의  
   *가중치가 없는 그래프 기준
```
adj = list()

def bfs(start):
  discovered = [False]*len(adj)
  q = list()
  order = list()
  
  discovered[start] = True
  q.append(start)
  
  while q:
    #큐에 먼저 들어간 노드를 방문
    here = q.pop(0)
    order.append(here)
    
    for next_node in adj[here]:
      #아직 발견되지 않았다면
      if !discovered[next_node]:
        #방문하기 위해 큐에 저장
        q.append(next_node)
        discovered[next_node] = True
        
  return order
```
- 모든 정점은 세 개의 상태를 순서대로 거쳐감
   1. 아직 발견되지 않은 상태
   2. 발견 되었지만 아직 방문되지는 않은 상태 - 큐에 저장
   3. 방문된 상태
   
- 시간 복잡도
   - 인접 리스트: $O(|V|+|E|)$
   - 인접 행렬: $O(|V|^{2})$

### 너비 우선 탐색과 최단거리
- 너비 우선 탐색 스패닝 트리(BFS Spanning Tree): 탐색에서 새 정점을 발견하는데 사용했던 간선들만 모은 트리
- BFS 스패닝 트리는 시작점으로부터 다른 모든 정점까지의 최단 경로를 표현함
```
adj = list()
distanse = [-1]*len(adj)
parent = [-1]*len(adj)

def bfs2(start):
  q =list()
  distanse[start] = 0:
  parent[start] = start
  q.append(start)
  while q:
    here = q.pop(0)
    for next_node in adj[here]:
      if distance[next_node] == -1:
        q.append(next_node)
        distance[next_node] = distance[here] + 1
        parent[next_node] = here
   
#시작점에서 v까지의 경로 반환
def shortest_path(v):
  path = [v]
  
  #시작점만 부모와 자신이 같음
  while parent[v] != v:
    v = parent[v]
    path.append(v)
    
  path = [::-1] #path.reverse()
  return path
```
