# 03 그리디

## 1) 당장 좋은 것만 선택하는 그리디
- 그리디(Greedy) 알고리즘은 현재 상황에서 지금 당장 좋은 것만 고르는 탐욕적 방법
- 코딩 테스트에서 그리디 알고리즘 유형 문제는 문제를 풀기 위한 최소한의 아이디어를 떠올릴 수 있는 능력을 요구함  
  특정한 문제를 만났을 때 단순히 현재 상황에서 가장 좋아 보이는 것만을 선택해도 문제를 풀 수 있는지를 파악할 수 있어야 함  
- 기준에 따라 좋은 것을 선택하는 알고리즘이므로 문제에서 '가장 큰 순서대로'와 같은 기준을 알게 모르게 제시함  
$\Rightarrow$ 그리디 알고리즘 문제는 자주 정렬 알고리즘과 짝을 이뤄 출제됨

#### 예제 3-1 거스름돈

- 문제  
  - 손님에게 N원을 받고 거스름돈이 500원, 100원, 50원, 10원 단위로 있을 때, 손님에게 거슬러줘야 할 동전의 최소 개수 구하기  

- 풀이  
  - 가장 큰 화폐 단위부터 돈을 거슬러 줌  
  ```
  N = input()
  count = 0
  
  coin_types = [500, 100, 50, 10]
  
  for coin in coin_types:
    count += N//coin #몫: 해당 화폐로 거슬러줄 수 있는 동전 개수
    N %= coin #나머지: 거슬러주고 남은 돈
  
  print(count) 
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
