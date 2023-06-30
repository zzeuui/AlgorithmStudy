# 05 DFS/BFS

## 1) 꼭 필요한 자료구조 기초
- 대표적인 탐색 알고리즘 DFS와 BFS를 이해하기 위해서는 스택과 큐, 재귀 함수에 대한 이해가 필요
- 스택과 큐는 삽입(push)와 삭제(pop)이라는 두 가지 핵심 함수로 구성됨
- 스택
  - 선입후출(First In Last Out) 또는 후입선출(Last In First Out) 구조
   - 기본 리스트에서 append()와 pop() 메서드 이용
   ```
  stack = list()
  stack.append(5)
  stack.pop()
  print(stack) #최하단 원소부터 출력
   print(stack[::-1]) #최상단 원소부터 출력
  ```
- 큐
  - 선입선출(First In First Out) 구조
  - collections 모듈의 deque 자료 구조 활용. 속도가 리스트에 비해 효율적이고, queue 보다 사용법이 간단함
  ```
  from collections import deque
  queue = deque()
  queue.append(5)
  queue.popleft()
  print(queue) #입력 순으로 출력
  queue.reverse() #역순
  print(queue) #최근 입력부터 출력
  queue_to_list = list(queue) #리스트형으로 변환
  ```
- 재귀 함수
  - 자기 자신을 다시 호출하는 함수
  ```
  def func(i):
    #재귀 함수 종료 조건과 return으로 종료   
    if i == 100:
      return

    #재귀 호출
    func(i+1)
  
  func(1)
  ```
  - 재귀 함수는 내부적으로 스택과 동일하여, 스택을 활용해야하는 상당수 알고리즘을 재귀 함수로 간편하게 구현 가능. DFS가 대표적인 예.
  - 또한 반목문을 재귀함수로 구현할 수 있는데, 이 경우 코드가 더욱 간결해짐.
  ```
  #iterative factorial
  ret = 1
  for i in range(1, n+1):
    ret *= i
  
  #recursive factorial
  def func(n):
    if n <= 1:
      return 1
    
    #n! = n *(n-1)!
    return n * func(n-1)
  ```  

## 2) 탐색 알고리즘 DFS/BFS
#### 그래프 표현 방식
- DFS와 BFS는 그래프 탐색 알고리즘으로, 그래프는 크게 2가지 방식으로 표현 가능
- 인접 행렬(Adjacency Matrix)
```
graph = [[0,7,5], 
         [7, 0, INF], 
         [5, INF, 0]]
```
- 인접 리스트(Adjacency List)
```
graph = [[(1,7) (2,5)], #노드 0에 연결된 노드 
         [(0,7)],       #노드 1에 연결된 노드
         [(0,5)]]       #노드 2에 연결된 노드
```
- 인접 행렬은 메모리 낭비, 인접 리스트는 속도가 느린 단점이 있음
$\Rightarrow$ 특정 노드와 연결된 모든 인접 노드를 순회해야하는 경우, 인접 리스트 방식이 메모리 공간 낭비가 적음

#### DFS
- Depth-First Search(깊이 우선 탐색): 그래프의 깊은 부분을 우선적으로 탐색하는 알고리즘
- 스택을 이용한 동작 과정
  - 탐색 시작 노드를 스택에 삽입하고 방문 처리
  - 스택 최상단 노드에 방문하지 않은 인접 노드가 있으면,해당 인접 노드를 스택에 삽입하고 방문 처리.  
    방문하지 않은 인접 노드가 없다면, 스택에서 최상단 노드 삭제
  - 위 두 과정을 더 이상 수행할 수 없을 때까지 반복
```
def dfs(node):
  visited[node] = True
  for nt_node in graph[node]:
    if not visited[nt_node]:
      dfs(nt_node)

graph = [[]] #인접 리스트 표현
visited = [False]*len(graph)

dfs(start_node)
```

#### BFS
- Breadth First Search(너비 우선 탐색): 가까운 노드부터 탐색하는 알고리즘
- 큐를 이용한 동작 과정
  - 탐색 시작 노드를 큐에 삽입하고 방문 처리
  - 큐에서 노드를 꺼내 해당 인접 노드 중 방문하지 않은 노드 모두 큐에 삽입 후 방문 처리
  - 위 두 과정을 더 이상 수행할 수 없을 때까지 반복
  ```
  from collections import deque
  graph = [[]] #인접 리스트 표현
  visited = [False]*len(graph)

  queue = deque()
  
  queue.append(start_node)
  visited[start_node] = True

  while queue:
    here = queue.leftpop()
    
    for nt_node in graph[here]:
      if not visited[nt_node]:
        queue.append(nt_node)
        visited[nt_node] = True

  ```

#### Tip
- 1차원 배열과 2차원 배열에서의 탐색 문제를 만날 경우 그래프 형식으로 바꾸어 DFS나 BFS로 해결하면 수월함
  - ex) 2차원 배열의 게임맵에서 캐릭터의 이동 문제

## 3) 음료수 얼려 먹기
- 문제
  - N*M 얼음틀이 존재, 0이 얼음틀 1이 칸막이
  - 0으로 표현된 얼음틀 개수 구하기
- 풀이
  - 책: 따로 그래프 표현을 만들지 않고 상하좌우에 바로 재귀적으로 접근
  ```
  n, m = map(int, input().split())
  graph = []
  for i in range(n):
    graph.append(list(map, int, input()))

  def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
      return False
  
    if graph[x][y] == 0:
      #방문처리
      graph[x][y] = 1
      #상하좌우 재귀적으로 호출
      dfs(x-1, y)
      dfs(x, y-1)
      dfs(x+1, y)
      dfs(x, y+1)
      return True 

    return False

  ret = 0
  for i in range(n):
    for j in range(m):
      if dfs(i, j) == True:
        ret += 1
  print(ret)
  ```
  - 스스로: 부분 그래프 구하기는 바로 떠오르고 금방 작성했는데 그래프 표현 구현한다고 한 시간 걸림,,
  ```
  from collections import defaultdict

  n, m = map(int, input().split())

  conet = list()
  for _ in range(n):
    conet.append(list(input()))

  dxy = [(-1, 0), ( 1, 0), (0, -1), (0, 1)]

  g = defaultdict(list)

  for i in range(n):
    for j in range(m):
      if conet[i][j] == '0':
        g[i*m+j].append((i*m+j))
        for x, y in dxy:
          ni, nj = i+x, j+y
          if ni > -1 and nj > -1 and ni < n and nj < m and conet[ni][nj]=='0':
            g[i*m+j].append((ni)*m+nj)

  g = {k:set(v) for k, v in g.items()}
  visited = [False] * (n*m)

  def dfs(here):
    visited[here] = True

    for nt_node in g[here]:
      if not visited[nt_node]:
        dfs(nt_node)

  cnt = 0
  for k, _ in g.items():
    if not visited[k]:
      dfs(k)
      cnt += 1

  print(cnt)
  ```

## 4) 미로 탈출
- 문제
  - N*M: 0은 괴물, 1은 길
  - 괴물을 피해 상하좌우로 이동할 때 (1, 1)에서 (N, M)까지 가는 최단 경로 구하기
  - 시작칸과 마지막 칸까지 경로에 포함
- 풀이
  - 책: 어차피 graph가 0과 1로 이뤄진 인접 행렬 표현의 그래프로 주어지기 때문에 나처럼 따로 distance 배열을 만들지 않고 graph에서 더해가는 식으로 진행함. 이렇게 할 경우 graph의 길로 표시된 '1'이 거리로 바뀌기 때문에 방문 여부도 따로 처리할 필요 없음.
  ```
  ...
  #해당 노드를 처음 방문한 경우 최단 거리 기록
  if graph[nx][ny] == 1:
    graph[nx][ny] = graph[x][y] + 1
    queue.append((nx, ny))
  ...
  ```
  - 스스로: 3번 문제에서 배운대로 graph에서 바로 인접 노드 접근하고 방문 표시는 했는데, distance는 따로 저장함. 시간 안에 풀음.
  ```
  from collections import deque

  n, m = map(int, input().split())
  g = list()
  for _ in range(n):
    g.append(list(input()))

  distance = [[0]*m for _ in range(n)]

  queue = deque()
  queue.append((0, 0))
  g[0][0] = '0'

  while queue:
    x, y = queue.popleft()

    for i in [1, -1]:
      nx, ny = x+i, y+i
      if nx > -1 and nx < n and g[nx][y] == '1':
        g[nx][y] = '0'
        queue.append((nx, y))
        distance[nx][y] = distance[x][y] + 1

      if ny > -1 and ny < m and g[x][ny] == '1':
        g[x][ny] = '0'
        queue.append((x, ny))
        distance[x][ny] = distance[x][y] + 1

  print(distance[n-1][m-1] + 1)
  ``` 
