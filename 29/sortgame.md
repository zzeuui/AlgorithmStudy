### 첫번째 방법
- 그래프 생성
   - 배열을 각 정점으로 표현
   - 한 배열에서 부분 구간을 뒤집어 만들어진 배열들을 간선으로 연결
     - {1, 2, 3} - {2, 1, 3} - {2, 3, 1} - {3, 2, 1} - ...
     - {1, 2, 3} - {1, 3, 2} - {3, 1, 2} - ...
   - 암시적 그래프 표현 사용  
     - 처음 주어진 배열에서 부분 구간을 뒤집으며 생성된 배열과 간선을 연결.생성된 배열에서 다시 부분 구간을 뒤집어 생성된 배열과 간선 연결하며 그래프 생성.

- 코드1
```
from collections import defaultdict

#perm: 처음 주어진 배열
def bfs(perm):
  n = len(perm)
  
  goal = sorted(perm)
  
  q = list()
  distance = {}
  
  distance[str(perm)] = 0
  q.append(perm)
  
  while q:
    here = q.pop(0)
    
    #현재 배열이 정렬된 배열이라면 종료하고 현재 배열까지의 거리 반환
    if here == goal:
      return distance[str(here)]
    
    #시작 배열에서 현재 배열까지의 거리
    cost = distance[str(here)]
    
    #현재 배열에서 가능한 모든 구간 뒤집기
    for i in range(n):
      for j in range(i+2, n+1):
        part_re = here[:i] + list(reversed(here[i:j])) + here[j:]
        if distance[str(part_re)] == 0:
          distance[str(part_re)] = cost + 1
          q.append(part_re)
          
  return -1 
```

- 한계점 
    - 한 케이스에 대해서 최악의 경우 $n!$의 시간 복잡도를 가짐. 모든 케이스를 시간 안에 풀기 어려움 *현재 주어진 문제에서는 1000개
    - 숫자가 달라도 상대적 크가 같은 배열의 답은 같음
       - {30, 40, 10, 20}과 {3, 4, 1, 2}의 답은 같음
    - 양방향 그래프이기 때문에 시작 정점에서 목표정점으로, 목표정점에서 시작정점으로 가는 최단 거리가 같음  
       $\Rightarrow$ 정렬된 배열을 원래 배열로 바꾸는 연산 수 == 원래 배열에서 정렬된 배열로 바꾸는 연산 수
       
- 코드2
    - 배열의 최대 길이 n이 주어졌을 때, 정렬된 배열 [0] or [0, ..., n-1]에서 다른 모든 상태까지 도달하는 데 필요한 뒤집기 연산 수를 미리 계산함
    - 입력받은 배열을 상대적 크기를 유지하며 배열의 요소를 0과 n-1 사이의 값이 되도록 변환
    - 미리 계산한 연산 수 반환
```
from collections import defaultdict

to_sort = defaultdict(int)

def precalc(n):
   perm = [ i for i in range(n) ]
   
   q = list()
   q.append(perm)
   to_sort[str(perm)]
   
   while q:
      here = q.pop(0)
      cost = to_sort[str(here)]
      for i in range(n):
         for j in range(i+2, n+1):
            part_re = here[:i] + list(reversed(here[i:j])) + here[j:]
            if to_sort[str(part_re)] == 0:
               to_sort[str(part_re)] = cost + 1
               q.append(part_re)
               
def solve(perm):
   n = len(perm)
   fixed = [-1]*n
   for i in range(n):
      smaller = 0
      for j in range(n):
         if perm[j] < perm[i]: smaller += 1
      fixed[i] = smaller
      
   return to_sort[str(fixed)]
```
