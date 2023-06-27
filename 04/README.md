# 04 구현

## 1) 아이디어를 코드로 바꾸는 구현  
- 프로그래밍 문법을 정확하게 숙지하지 못했거나 라이브러리 사용 경험이 부족하면 구현 유형 문제를 풀 때 불리함
  - ex) 순열 문제의 경우 itertools와 같은 표준 라이브러리로 구현할 수 있음
- 리스트의 크기가 1,000만 이상이라면 메모리 제한에 걸릴 수 있음
- 1초에 2,000만 번의 연산을 수행하다고 가정하면 크게 무리없음
  - ex) 데이터가 100만 개라면 시간복잡도  O(NlogN)이내의 알고리즘을 이용해야함
- Pypy3는 파이썬3 문법을 그대로 지원하고, 대부분 파이썬3보다 실행 속도가 더 빠름 $\Rightarrow$ 코테에서 Pypy3 지원하는 지 확인  

#### 예제 4-1 상하좌우

- 문제  
  - NxN 공간에서 상하좌우 이동 계획서가 주어졌을 때 최종 좌표 구하기.
  - 공간을 벗어나는 이동은 무시하고, 왼쪽 위 좌표가 (1,1), 오른쪽 아래좌표가 (N,N)임

- 풀이  
  - 시뮬레이션 유형으로 분류되는 구현 문제. 코테에서 시뮬레이션 유형, 구현 유형, 완전탐색 유형은 서로 유사한 점이 많음.
  ```
  n = int(input())
  plans = input().split()
  x, y = 1, 1

  # 1
  for p in palns:
    if p == 'R' and x < n: x += 1
    elif p =='L' and x  > 1: x -= 1
    elif p == 'U' and y > 1: y -= 1
    elif p =='D' and y < n: y += 1
  print(y, x)

  # 2 in book
  dx = [0, 0, -1, 1]
  dy = [-1, 1, 0, 0]
  move_types = ['L', 'R', 'U', 'D']

  for plan in plans:
    for i in range(len(move_types)):
      if plan == move_types[i]:
        nx = x + dx[i]
        ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
      continue
    x, y = nx, ny

  print(x, y)
  ```
#### 예제 4-2 시각

- 문제  
  - 정수 N이 주어졌을 때, 00시 00 분 00초부터 N시 59분 59초까지의 시각 중 3이 포함된 시각 수 구하기 

- 풀이  
  - 완전탐색으로 품. 24x60x60=86,400가지밖에 존재하지 않음
  ```
  h = int(input())
  cnt = 0

  # 1
  for i in range(h+1):
    for j in range(60):
      for k in range(60):
        temp = str(i)+str(j)+str(k)
        if '3' in temp: cnt += 1

  print(cnt)
  ```

## 2) 왕실의 나이트 
- 문제  
  - 행 1~8, 열 a~h로 표현되는 8X8 좌표 평면이 주어졌을 때 나이트가 이동할 수 있는 경우의 수 구하기
  - 나이트는 2가지 경우로 이동 가능
    - 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동하기
       - 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동하기  
  
- 풀이 
  ```
  n = input()
  x, y = ord(n[0]), int(n[1])
  dx = [2, 2, -2, -2, 1, -1, 1, -1]
  dy = [-1, 1, -1, 1, -2, -2, 2, 2]

  cnt = 0
  for mx, my in zip(dx, dy):
    nx = x + mx
    ny = y + my

    if nx > ord('h') or nx < ord('a') or ny < 1 or ny > 8:
        continue
    else:
        cnt += 1

  print(cnt)
  ```

## 3) 숫자 카드 게임
- 문제
  - 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 게임
  - 행을 먼저 선택하고, 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑아야 함
- 풀이  
  - 각 행마다 가장 작은 수를 찾은 뒤에 그 수 중에서 가장 큰 수를 찾음
  ```
  N, M = map(int, input().split())
  cards = list()

  # 1
  for _ in range(N):
    card = min(list(map(int, input().split())))
    cards.append(card)
  print(max(cards))

  # 2 in book
  ret = 0
  for _ in range(N):
    card = min(list(map(int, input().split())))
    ret = max(ret, card)
  print(ret)
  ```
## 4) 1이 될 때까지
- 문제
  - N이 K로 나눠 떨어지면 N/K를 수행하고 아니면 N-1을 수행
  - N이 1이 될 때까지 위의 과정을 수행한 횟수
- 풀이
  ```
  N, K = map(int, input().split())
  ret = 0

  # 1
  while N > 1:
    if N%K == 0:
      N /= K
      ret += 1
    else:
      N -= 1
      ret += 1
  print(ret)
  
  # 2 in book
  while True:
    target = (N//K) * K
    ret += (N - target) # N을 K로 나누었을 때 나머지. 즉, K로 나누기 위해 1씩 빼야할 수
    N = target
    #N이 K보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
    if N < K:
      break
    #K로 나누기
    ret += 1
    N //= K

  #K로 더이상 못 나누는 1씩 빼야할 나머지
  ret += (N-1)
  print(ret)
  ```
