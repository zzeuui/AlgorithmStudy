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

- 간단한 예제
   1. 두 정점의 연결 여부  
     dfs(u) 수행 후 visited 참조 $\Rightarrow$ u로부터 각 정점에 갈 수 있는지 확인 가능
   2. 그래프 내의 연결된 부분집합의 개수  
     dfsAll()에서 dfs()를 호출한 횟수
   3. 위상 정렬(topological sort)  
     dfsAll()의 내부의 dsf()가 종료할 때마다 현재 정점 번호 기록후, dsfAll()이 종료하면 기록된 순서를 뒤집기

### 오일러 서킷과 트레일, 해밀토니안 경로
1. 오일러 서킷(Euler circuit)
   - 그래프의 모든 간선을 한 번씩 지나서 시작점으로 돌아오는 경로
   - 모든 정점들이 짝수점일 경우 존재함, *들어오는 간선 수와 나가는 간선 수가 일치해야함
     - 한 정점의 인접한 간선의 수를 해당 정점의 차수(degree)라고 부르고, 차수가 홀수면 홀수점이고 짝수면 짝수점이라고함
   - 이미 지난 간선 정보는 삭제되도록 코드 구현

2. 오일러 트레일(Euler circuit)
   - 그래프의 모든 간선을 한 번씩 지나면서 시작점과 끝점이 다른 경로
   - 시작점의 경우 들어오는 간선 수가 하나 적어야 하고, 끝점의 경우 나가는 간선 수가 하나 적어야 함. 즉, 시작점과 끝점에 하나의 간선을 추가했을 때 그래프의 모든 정점이 짝수점이 되어야함.

3. 해밀토니안 경로(Hamiltonian path)
   - 그래프의 모든 정점을 한 번씩 지나는 경로
   
### 그래프 간선의 분류
- 깊이 우선 탐색을 하면, 그래프의 정점들과 DFS가 따라가는 간선들로 구성된 트리가 만들어짐. 이러한 트리를 *깊이 우선 탐색 스패닝 트리* 혹은 
*DFS spanning tree*라고 함
- 그래프 간선의 분류
   - 트리 간선(tree edge): 스패닝 트리에 포함된 간선
   - 순방향 간선(forword edge): 스패닝 트리의 선조에서 자손으로 연결되지만 트리 간선이 아닌 간선
   - 역방향 간선(back edge): 스패닝 트리의 자손에서 선조로 연결되지만 트리 간선이 아닌 간선
   - 교차 간선(cross edge): 스패닝 트리에서 선조와 자손 관계가 아닌 정점들 간에 연결된 트리 간선이 아닌 간선
 
- 무향 그래프 간선의 분류
   - 모든 간선이 양방향으로 통행 가능
   - 교차 간선이 존재하지 않음
   - 순방향 간선과 역방향 간선의 구분이 없음

- 그래프 알고리즘의 이해
   - (u, v)가 트리 간선이라면 dfs(v)가 dfs(u)보다 먼저 종료되어야함
   - (u, v)가 순방향 간선이라면 v가 u의 자손임으로 dfs(u)가 먼저 호출되고, dfs(v)가 먼저 종료되어야함
   - (u, v)가 역방향 간선이라면 v가 u의 선조임으로 dfs(v)가 먼저 호출되고, dfs(u)가 먼저 종료되어야함
   - (u, v)가 교차 간선이라면 dfs(v)가 호출·종료되고나서 dfs(u)가 호출되어야함. 
   - 역방향 간선이 존재하면, 사이클이 존재함  
     $\Rightarrow$ DFS 과정에서 제일 처음 만나는 사이클의 한 정점이 u이고 u가 v로 향한다고 했을 때, dfs(u)가 종료되기 전에 dfs(v)에 의해 u를 다시 방문하게 되면 (u, v)는 역방향 간선이고 사이클이 존재함을 의미함.

- 간선의 분류 구현
   - 단순히 정점을 방문했다는 정보(visited)가 아니라, 배열읈 사용해 해당 정점을 발견한 순서에 대한 정보(discovered)를 저장함.
   - 그리고 교차 간선 구분을 위해 종료 순서(finised)를 저장함
   
### 예제
1. 절단점 찾기 알고리즘
   - 그래프의 절단점(cut vertex): 인접한 간선들을 모두 지웠을 때 그래프의 컴포넌트가 두 개 이상으로 나눠지는 정점
   1. 깊이 우선 탐색 수행으로 DFS 스패닝 트리 생성
   2. 임의의 정점 u의 선조와 자손 사이에 역방향 간선이 하나라도 없다면 u는 절단점이 될 수 있음  
     u의 선조와 자손들이 전부 역방향 간선으로 연결되면 u는 절단점이 될 수 없음
   3. u가 스패닝 트리의 루트라 선조가 없더라도, 자손이 둘 이상 존재해야 절단점이 될 수 있음.  
   $\Rightarrow$ 모든 정점의 발견 순서를 비교하여 선조자손 관계(역방향 간선)를 찾아 냄
   - 이중 결합 컴포넌트(binconnected component): 무향 그래프에서 절단점으로 포함하지 않는 서브그래프
   
2. 다리 찾기
   - 어떤 간선을 삭제했을 때, 두 개의 컴포넌트로 쪼개질 경우 해당 간선을 다리(bridge)라고 함
   - 다리는 항상 트리 간선이기 때문에, 트리 간선만 다리인지 판단하면 됨
   - (u, v)가 다리이기 위해서는, v와 v의 서브트리에서 역방향 간선으로 u보다 높은 정점에 갈 수 없어야함  
   $\Rightarrow$ v와 그 자손들에서 역방향 간선으로 닿을 수 있는 정점의 최소 발견 순서가 u 후라면 (u, v)는 다리임
 
3. 강결합 컴포넌트 분리(strongly connected components, SCC)
   - 방향 그래프의 두 정점 u와 v에 대해 양 방향으로 가는 경로가 모두 있을 때 두 정점은 같은 SCC
   - SCC들을 정점으로 하고 SCC 사이를 연결하는 간선으로 DAG를 생성할 수 있음  
   $\Rightarrow$ 각 SCC를 표현하는 정점들을 갖는 새로운 그래프로 기존 그래프를 압축(condensation)을 할 수 있음
   - 타잔(Tarjan) 알고리즘
   1. 깊이 우선 탐색 수행으로 DFS 스패닝 트리 생성
   2. 트리간선 (u, v)가 존재할 때, v를 루트로 하는 서브트리에서 v보다 먼저 발견된 정점으로 가는 역방향 간선이 있으면 (u, v)를 절단하면 안됨
   3. 역방향 간선이 없더라도, v보다 먼저 발견되었으면서 SCC로 묶여 있지 않은 정점으로 가는 교차 간선이 있으면 (u, v)를 절단하면 안됨
   ```
    import sys
    import collections

    input = sys.stdin.readline
    sys.setrecursionlimit(10**7)

    th = 0
    sccCounter = 0

    def scc(here):
      global th, sccCounter
      
      #현재 노드가 몇번째로 발견되었는지 기록 
      discovered[here] = th
      th += 1
      cur = discovered[here]
      
      # stack에 현재 노드를 넣고,
      # 현재 노드의 후손들은 모두 현재 노드 이후에 스택에 들어감 
      stack.append(here)

      for next_node in G[here]:
          #방문한 적이 없는 노드라면 탐색함 ==> (here, next_node)는 트리간선이 됨
          if discovered[next_node] == -1: 
              parent = min(cur, scc(next_node))
          #elif: 이미 DFS로 방문한 적은 있지만, 다시 방문한 노드 즉, 현재 노드와 교차 간선일 경우 
          #on_stack[next_node] == -1: 그리고 SCC에 포함되지 않을 경우
          #here과 next_node 중 누가 먼저 발견되었는지 검사
          elif on_stack[next_node] == -1: 
              parent = min(cur, discovered[next_node])
              
      # 1. 트리간선으로 연결된 정점들 중 가장 먼저 발견되었을 때
      # 2. 교차 간선을 검사했을 때 현재 노드가 가장 먼저 발견되었을 때
      if parent == cur:
          while True:
              t = stack.pop() #스택에 있는 모든 후손과 자신을 차례로
              on_stack[t] = sccCounter #SCC에 포함함. sccCounter는 현재 몇번째 SCC인지 구분하기 위해 사용
              if t == here:
                  break

          sccCounter += 1

      return parent

    if __name__=='__main__':
      V, E = map(int, input().rstrip().split())
      G = collections.defaultdict(list)

      for _ in range(E):
          u, v = map(int, input().rstrip().split())
          G[u].append(v)

      discovered = [-1]*V
      on_stack = [-1]*V
      stack = list()

      for i in range(V):
          if discovered[i] == -1:
              scc(i)
   ```
