### CHILDRENDAY
- 목표
   -  다음 세가지를 만족하는 최소의 자연수 $c$ 찾기
      
   1. $n+m \leq c$, $n$은 총인원 $m$은 욕심쟁이수
   2. $c$ mod $n = m$
   3. $c$는 주어진 $d$에 포함된 숫자들로만 구성됨

- 문제정의
   -  세번째 조건에 따라 $c$를 앞에서부터 한 자리씩 생성. 현재 숫자 $c$에 $x$를 붙여 다음 숫자를 생성
      - $c \times 10 + x$
   -  두번째 조건에 따라 $(c \times 10 + x)$ mod $n = m$인지 확인
      - 나머지 연산의 분배 법칙에 의해,  
        $(c \times 10 + x)$ mod $n$ = $((c$ mod $n)\times 10 + x)$ mod $n$  
        로 정의되고, 그러므로 $c$ mod $n$을 확인하면 됨
        
- 그래프 모델링
   - $c$ mod $n = a$, $(0 \leq a \leq n-1)$  
   - 정점 $a$와 정점 $a \times 10 + x$ mod $n$을 $x$로 번호 매긴 간선으로 연결
   - 정점 0에서 정점 m으로 가는 최단경로의 간선 번호를 모아 $c$를 생성
   - 최단 경로 $c$가 여러 개일 경우 간선 번호가 사전순으로 가장 작은 경우를 선택  
     $\Rightarrow$ 너비 우선 탐색을 할 때 간선의 번호가 증가하는 순서로 검사해 BFS 스패닝 트리 생성.  
     스패닝 트리의 경로가 사전순으로 가장 작은 최단 경로임

- 마지막 조건 추가 **완전히 이해하지 못함 
   - $c$ mod $n = m$에서 $m$은 $n+m$의 $m$을 의미함. $n$번의 나머지 연산이 이뤄진 후에, 계속 $c$에 대해 나머지 연산을 수행하고서 $m$을 만나야함.
   - 즉, 첫번째 조건  $n+m \leq c$을 만족하기 위해 n으로 나눈 나머지마다 두 개의 정점을 생성
      - 지금까지 만든 정점 수가 $n$ 미만인 경우
      - 지금까지 만든 정점 수가 $n$ 이상인 경우  
      $\Rightarrow$ 지금까지 만든 정점 수가 $n$ 이상이어야 함.  
      $+$ $n$번 이상에 정점 $m$에 도달할 수 있어야함
      
```
def append(here, edge, mod):
   there = int(str(here*10)[:-2] + str(edge))
   #회색 정점
   if there >= mod: return mod + there % mod
   #흰색 정점
   return there % mod
   
def gifts(d, n, m):
   d.sort()
   parent = [-1]*(2*n)
   choice = [-1]*(2*n)
   q = list()
   
   parent[0] = 0
   q.append(0)
   
   while q:
      here = q.pop(0)
      for i in d:
         there = append(here, i, n)
         if parent[there] == -1:
            parent[there] = here
            choice[there] = i
            q.append(there)
   
   # n번 이상 정점을 생성하고, m에 도달할 수 있어야 하는데
   # 그렇지 못했을 때
   if parent[n+m] == -1: return "IMPOSSIBLE"
   
   ret = list()
   here = n+m
   while parent[here] != here:
      ret.append(str(choice[here]))
      here = parent[here]
   ret = int(''.join(ret[::-1]))
   return ret
```
