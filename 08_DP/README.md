# 08 다이나믹 프로그래밍

## 1) 다이나믹 프로그래밍(Dynamic Programming)
#### 개념
- 동적계획법
- 메모리 공간을 더 사용해 연산 속도를 증가시키는 방법
- 큰 문제를 작게 나누고, 같은 문제라면 한 번씩만 풀어 문제를 효율적으로 해결하는 알고리즘
- DP 사용 조건
  - 큰 문제를 작은 문제로 나눌 수 있다
  - 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일하다

#### 메모이제이션(Memoization)
- DP 구현 방법 중 한 종류 캐싱(Caching)이라고도 함
- 한 번 구한 결과를 메모리 공간에 저장하고, 같은 식을 다시 호출하면 저장한 결과를 그대로 호출함
- 예제
  - 피보나치 수열(재귀적): 큰 문제를 위해 작은 문제를 호출하는 top-down 방식
  ```
  d = [0]*100 # 메모이제이션 리스트
  
  def fibo(x):
    if x == 1 or x == 2:
      return 1
    if d[x] != 0:
      return d[x]
    d[x] = fibo(x-1)+fibo(x-2)
    return d[x]
  ```
  - 피보나치 수열(반복적): 작은 문제부터 답을 도출하는 bottom-up 방식
  ```
  d = [0]*100 #메모이제이션 리스트

  d[1], d[2] = 1, 1
  n = 99

  for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]
  ```

#### 응용
- DP의 전형적인 형태는 bottom-up 방식
- 특정한 문제를 완전 탐색 알고리즘으로 접근했을 때 시간이 매우 오래걸리면 DP를 적용 가능 여부 혹은 해결하고자 하는 부분 문제들의 중복 여부 파악
- 우선 재귀적으로 구현하고 => 메모이제이션 적용하여 코드 개선
- 재귀함수 스택 크기가 한정되어있기때문에, 가능하다면 bottom-up 방식으로 구현
  - sys 라이브러리의 setrecursionlimit() 함수를 호출해 크기 제한을 완화할 수 있음

## 2) 1로 만들기
- 문제
  - 가능한 4가지 연산이 주어졌을 때, 가장 적은 연산으로 1만들기
  - x가 5로 나눠 떨어지면 5로 나눔, 3으로 나눠 떨어지면 3으로 나눔, 2로 나눠 떨어지면 2로 나눔. 앞의 3가지 경우에 모두 해당되지 않으면 1을 뺌
- 풀이
  - a_i = min(a_i-1, a_i/2, a_i/3, a_i/5)+1
  - 완전탐색으로 구하고, DP로 개선하는데 d[x] < i일 때만 d[i]를 개선하는 조건을 안 넣어서 헤맴. 재귀적으로 풀어서 X가 6500만 돼도 프로그램이 안돌아감.., 52분
  ```
  import sys
  sys.setrecursionlimit(10**7)
  
  def compute_x(x, i):
    x = int(x)
    ret1, ret2, ret3, ret4 = float("inf"), float("inf"), float("inf"), float("inf")
    
    if x == 1: return i
    
    i += 1
    if d[x] != 0 and d[x] < i: return d[x]

    if x%5 == 0:
      ret1 = compute_x(x/5, i)
    if x%3 == 0:
      ret2 = compute_x(x/3, i)
    if x%2 == 0:
      ret3 = compute_x(x/2, i)
    ret4 = compute_x(x-1, i)

    d[x] = min(ret1, ret2, ret3, ret4)
    return d[x]

  x = int(input())
  d = [0]*(x+1)
  print(compute_x(x, 0))
  ```
  - 책
    - bottom up 방식
    - 나는 x와 결과값을 따로 구하고 리스트에 저장하고 또 따로 리스트를 검사했는데,
    - 책은 리스트의 인덱스가 어차피 x니깐 인덱스 자체를 계산하고, 그 인덱스 값이 어차피 결과값이니깐 리스트 값을 가지고 바로 검사함.
  ```
  x = int(input())
  d = [0]*30001

  for i in range(2, x+1):
    # 현재의 수에서 1을 빼는 경우
    d[i] = d[i-1] + 1
    #현재의 수가 2로 나누어 떨어지는 경우
    if i%2 == 0:
      d[i] = min(d[i], d[i//2] + 1)
    if i%3 == 0:
      d[i] = min(d[i], d[i//3] + 1)
    if i%5 == 0:
      d[i] = min(d[i], d[i//5] + 1)
  
  print(d[x])
  ```

## 3) 개미 전사
- 문제
  - 식량창고(수열)에서 한 칸 이상 떨어진 식량(숫자)들끼리 더했을 때 가장 큰 값
- 풀이
  - 특정 i번째 식량창고에 대해서 털지 안털지, 2가지 경우에 대해서만 확인하면 됨
  - (i-1)번째 식량을 털면, 현재 식량 창고를 털 수 없음. (i-2)번째 식량을 털면, 현재 식량창고를 털 수 있음. 두 가지 경우 중 큰 값을 선택.
  - i번째 해를 구할 때 i-3번째까지 고려할필요가 없음. 이미 i-1과 i-2를 구하는 과정에서 고려되었기 때문에 i는 i-1과 i-2만 신경쓰면됨.
  - 나: 모든 경우의 수를 직접 손을 그려보다가, i가 3이상일 때 i번째 경우에 대해서 두 가지 경우밖에 안나오는 사실을 발견함. 25분
  ```
  """"
  total[2] = total[0] + store[2]

  total[3] = total[1] + store[3]
  total[3] = total[0] + store[3]

  total[4] = total[1] + store[4]
  total[4] = total[2] + store[4]

  total[5] = total[3] + store[5]
  total[5] = total[2] + store[5]
  """
  n = int(input())
  store = list(map(int, input().split()))
  total = [0]*n

  # 1
  total[0], total[1] = store[0], store[1]
  total[2] = total[0] + store[2]

  i = 3
  while i < n:
    total[i] = max(total[i-2] + store[i], total[i-3] + store[i])
    i += 1

  print(max(total[-2], total[-1]))

  # 2 in book
  total[0] = store[0]
  total[1] = max(store[0], store[1])
  for i in range(2, n):
    total[i] = max(total[i-1], total[i-2]+store[i])
  
  print(total[n-1])
  ```

## 4) 바닥 공사
- 문제
  - N*2의 바닥을, 2*1, 1*2, 2*2 덮개로 채울 수 있는 경우의 수
- 풀이
  - a_i = a_i-1 + a_i-2 * 2 = a_i-1 + a_i-2 + a_i-2
  - 나: a_i = a_i-1 + (a_i-2 + 1)로 생각함, 오답 37분
  ```
  n = int(input())
  d = [0]*(n+1)

  # 1 오답
  d[0] = 1
  d[1] = 1
  for i in range(2, n+1):
    d[i] = (d[i-1] + d[i-2] + 1) % 796796

  # 2 in the book
  d[1] = 1
  d[2] = 3
  for i in range(3, n+1):
    d[i] = (d[i-1] + 2*d[i-2]) % 796796

  print(d[n])
  ```

## 5) 효율적인 화폐 구성
- 문제
  - N개의 여러 단위 화폐가 주어졌을때, M원을 만들 수 있는 최소한의 화폐 개수
- 풀이
  - 금액 i를 만들 수 있는 최소한의 화폐 개수를 a_i, 화폐의 단위를 k라고 했을 때 다음의 점화식 작성 가능. a_i-k는 i-k를 만들 수 있는 최소한의 화폐 개수
  - 나: 똑같은 개념인데 top-down 방식으로 작성. 숫자가 조금만 커져도 프로그램이 안돌아감. DP 풀 때 bottom-up 방식으로 생각하고 구현하는 연습 좀 해야할 듯. 20분
  - 그리고 재귀적으로 구현한 걸 다시 어떻게 모든 화폐 단위에 대해서 반복적으로 계산하지 했는데, 한 화폐 단위 마다 계속해서 앞부터 빼가는 식으로 진행. 그리고 다음 화폐 단위도 같은 방식으로 진행하면, 각 인덱스에 앞서 계산한 정보가 담겨있기 때문에 결국 모든 경우의 수에 대해서 탐색할 수 있게 됨.
    - ex) 화폐단위 2 => 인덱스 i의 변화: 0(2-2), 1(3-2), 2(4-2), 3(5-2)...
  ```
  n, m = map(int, input().split())
  coin = list()
  for _ in range(n):
    coin.append(int(input()))

  # 1 
  d = [float("inf")]*(m+1)

  def f(m, i):
    if m == 0:
      return i
    for c in coin:
      if m-c >= 0:
        d[m] = min(d[m], f(m-c, i+1))
    return d[m]
  f(m, 0)
  if d[m] != float('inf'): print(d[m])
  else: print(-1)

  # 2 in the book
  d = [10001]*(m+1)
  d[0] = 0
  for i in range(n):
    for j in range(coin[i], m+1):
      if d[j-coin[i]] != 10001:
        d[j] = min(d[j], d[j-coin[i]] + 1)

  if d[m] == 10001: print(-1)
  else: print(d[m])
  ```