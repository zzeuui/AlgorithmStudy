# 그래프의 깊이 우선 탐색(Depth-First Search, DFS)

- 현재 정점과 인접한 간선들을 하나씩 검사하다가, 아직 방문하지 않은 정점으로 가는 간선을 선택하여 계속 탐색 진행. 막힌 정점에 도달하면 이전 경로로 돌아감
```
int adj = [[]] #인접 리스트 표현
bool visited = [false]*len(adj) #정점의 방문 여부

def dfs(int here):
  visited[here] = true
  
  for i in adj[here]:
    if not visited[i]:
      dfs(i)

def dfsAll():
  for i in range(len(adj)):
    if not visited[i]:
      dfs(i)
```

- 시간 복잡도
   - 인접 리스트: $O(|V|+|E|)$
   - 인접 행렬: $O(|V|^{2})$

### 예제
1. 두 정점의 연결 여부  
   dfs(u) 수행 후 visited 참조 $\Rightarrow$ u로부터 각 정점에 갈 수 있는지 확인 가능
2. 그래프 내의 연결된 부분집합의 개수  
   dfsAll()에서 dfs()를 호출한 횟수
3. 위상 정렬(topological sort)  
   dfsAll()의 내부의 dsf()가 종료할 때마다 현재 정점 번호 기록후, dsfAll()이 종료하면 기록된 순서를 뒤집기
