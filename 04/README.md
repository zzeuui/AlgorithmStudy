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
  - NxN 공간에서 상하좌우 이동 계획서가 주어졌을 때 최종 좌표 구하기.
  - 공간을 벗어나는 이동은 무시하고, 왼쪽 위 좌표가 (1,1), 오른쪽 아래좌표가 (N,N)임

- 풀이  
  - 시뮬레이션 유형으로 분류되는 구현 문제. 코테에서 시뮬레이션 유형, 구현 유형, 완전탐색 유형은 서로 유사한 점이 많음.
  ```
  ```
  
#### 그리디 알고리즘의 정당성
- 대부분의 문제는 그리디 알고리즘을 이용했을 때 '최적의 해'를 찾을 수 없을 가능성이 다분함  
- 그리디 알고리즘으로 문제의 해법을 찾았을 때는 정당한지 검토해야함  
ex) 화폐단위가 500원, 400원, 100원일 때 탐욕법의 해는 4개(500원, 100원x3)이고 최적해는 2개(400원x2)임  

## 2) 큰 수의 법칙
- 문제  
  - N 크기의 주어진 배열을 M번 더해 만들 수 있는 가장 큰 수 구하기. 이때 최대 K번 연속으로 더할 수 있음  
  
- 풀이1  
  ```
  N, M, K = map(int, input().split())
  nums = list(map(int, input().split()))
  nums.sort()
  
  ret = 0
  
  while M > 0:
    if M >= K:
      ret += K*nums[-1]
      M -= K
    else:
      ret += M*nums[-1]
      break
  
    if M == 0:
      break
    else:
      ret += nums[-2]
      M -= 1
  
  print(ret)
  ```

- 풀이2  
  - 반복되는 수열 파악. 가장 큰 수와 두번째로 큰 수가 더해질 때 특정한 수열 형태로 일정하게 반복해서 더해지는 특성이 존재
  - 여기서 반복되는 수열의 길이는 (큰 수를 $K$번 더하는 것 + 두번째로 큰 수를 한 번 더하는 것) = $(K+1)$임  
  - 수열이 반복되는 횟수 = $M//(K+1)$  
  - $i_1$ = 가장 큰 수의 등장 횟수 = 수열이 반복되는 횟수* $K$ + 수열이 반복되고 남은 더하기 횟수 = $(M//(K+1))*K + M mod (K+1)$
  - $i_2$ = 두번째로 큰 수의 등장 횟수 = 전체 더하기 횟수 - 가장 큰수의 등장 횟수 = $M - i_1$
  - 결과값 = $i_1$ \* 가장 큰 수 + $i_2$ * 두번째로 큰 수  
  ```
  N, M, K = map(int, input().split())
  nums = list(map(int, input().split()))
  nums.sort()

  count = M//(K+1) * K + M % (K+1)

  ret = 0
  ret += count * nums[-1]
  ret += (M - count) * nums[-2]

  print(ret)
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
