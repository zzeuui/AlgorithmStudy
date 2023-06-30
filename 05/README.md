ㅣ# 05 DFS/BFS

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
