# 06 정렬

## 1) 기준에 따라 데이터를 정렬
#### 선택 정렬(Selection Sort)
- 현재 정렬되지 않은 데이터 중에서 가장 작은 데이터를 이미 정렬된 데이터의 다음 위치의 데이터와 변경
- 다른 정렬 알고리즘에 비해 비효율적이지만 특정 리스트에서 가장 작은 데이터를 찾는 일이 코테에서 잦으므로 익숙해질 필요가 있음
```
for i in range(len(array)):
  min_ind = i
  for j in range(i+1, len(array)):
      if array[min_ind] > array[j]:
      min_ind = j
  array[i], array[min_ind] = array[min_ind], array[i] 
```

#### 삽입 정렬(Insertion Sort)
-  정렬하려는 데이터의 왼쪽에 있는 데이터들은 이미 정렬된 상태이므로, 왼쪽으로 한 칸씩 이동하다가 자기보다 작은 데이터를 만나면 그 앞에 데이터는 보지 않고 현재 위치에 데이터를 삽입함.
- 보통 비효율적이지만, 정렬의 거의 되어 있는 상태라면 정답 확률을 높일 수 있음
```
for i in range(1, len(array)):
  for j in range(i, 0, -1):
    if array[j] < array[j-1] # 한 칸씩 왼쪽으로 이동
      array[j], array[j-1] = array[j-1], array[j]
    else: #자기보다 작은 데이터를 만나면 그 위치에서 멈춤
      break
```

#### 퀵정렬(Quick Sort)
- 리스트에서 첫번째 데이터를 피벗(pivot)으로 설정한 다음, 왼쪽에서부터 피벗보다 큰 데이터를 찾고 오른쪽부터 피벗보다 작은 데이터를 찾음.   
그리고서 큰데이터와 작은 데이터를 교환함.   
큰 데이터와 작은 데이터가 엇갈린 위치에 존재하면, 작은 데이터와 피벗의 위치를 교환.   
피벗을 기준으로 왼쪽과 오른쪽 파트로 리스트를 분할하여 퀵정렬 다시 진행.   
- 이미 데이터가 정렬되어 있는 최악의 경우 $O(N^2)$의 시간복잡도를 가지지만, 기본 정렬 라이브러리를 이용하면 $O(NlogN)$을 보장함
```
def quick_sort(array):
  if len(array) <= 1:
    return array
  
  pivot = array[0]
  tail = array[1:]

  left_side = [x for x in tail if x <= pivot]
  right_side = [x for x in tail if x > pivot]
  
  return quick_sort(left_side) + [pivot] + quick_sort(right_side) 
```

#### 계수 정렬(Count Sort)
- 가장 큰 데이터와 작은 데이터의 차이가 1,000,000을 넘지 않고 정수 표현일 때 효과적으로 사용가능. 최악의 경우에도 N이 데이터의 개수, K가 최댓값일 때 $O(N+K)$의 시간복잡도 보장.
- 최댓값 크기 만큼의 0으로 초기화된 리스트 생성. 데이터를 하나씩 확인하며 데이터의 값과 동일한 인덱스의 데이터를 1씩 증가.
```
count = [0]*(max(array)+1)

for ind in array:
  count[ind] += 1

for c in count:
  for j in range(c):
    print(i, end=' ')
```

#### 파이썬의 정렬 라이브러리
- sorted(): 퀵 정렬과 동작 방식이 비슷한 병합 정렬 기반으로 구현. 최악의 경우에도 $O(NlogN)$ 보장. 
- sort(): 리스트 객체의 내장 함수
- 함수인 key 매개변수를 기분으로 정렬 가능
```
ret = sorted(array)
array.sort()

def setting(data):
  return data[1]

ret = sorted(array, key=setting)
```

#### 정렬 알고리즘에 대한 3가지 문제 유형
1. 정렬 라이브러리로 풀 수 있는 문제
2. 정렬 알고리즘의 원리에 대해서 물어보는 문제
3. 더 빠른 정렬이 필요한 문제: 퀵 알고리즘을 풀 수 없고 계수 정렬 등의 다른 알고리즘 사용하거나 기존의 알고리즘을 개선해야 풀 수 있는 문제

## 2) 위에서 아래로
- 문제
  - N개의 숫자가 주어졌을 때, 내림차순으로 출력
- 풀이
  - 주어진 데이터수가 적으므로 아무 정렬 알고리즘을 사용해도 무방. 기본 정렬 라이브러리가 효율적
  ```
  n = int(input())
  nums = list()
  for _ in range(n):
    nums.append(int(input()))
  
  # 1
  nums.sort()
  for e in nums[::-1]: print(e, end=' ')

  # 2 in book
  nums = sorted(nums, reverse=True)
  ```

## 3) 성적이 낮은 순서로 학생 출력하기
- 문제
  - N명의 학생 이름과 점수가 주어졌을 때, 점수를 기준으로 오름차순으로 학생 이름 출력
- 풀이
  - 최악의 경우 $O(NlogN)$을 보장하는 기본 정렬 라이브러리 사용
  ```
  n = int(input())
  rets = list()
  for _ in range(n):
    name, score = input().split()
    rets.append((name, int(score)))
  # 1
  def setting(data):
    return data[1]
  rets = sorted(rets, key=setting)
  for name, score in rets: print(name, end=' ')

  # 2 in book
  rets = sorted(rets, key=lambda x: x[1])
  ```

## 4) 두 배열의 원소 교체
- 문제
  - N개의 자연수 원소로 구성된 A와 B 배열이 존재할 때, K번의 우너소 교환을 통해 배열 A의 원소의 합이 최대가 되도록 함
- 풀이
  - 배열 A의 가장 작은 원소를 골라 배열 B의 가장 큰 원소와 교체
  - 미리 두 배열을 정렬하고, !배열 B의 원소가 큰 경우에만 교환!
  ```
  n, k = map(int, input().split())
  a = list(map(int, input().split()))
  b = list(map(int, input().split()))
  
  # 1
  for _ in range(k):
    a_ind = a.index(min(a))
    b_ind = b.index(max(b))

    if a[a_ind] < b[b_ind]:
      a[a_ind], b[b_ind] = b[b_ind], a[a_ind]

  # 2 in book
  a.sort()
  b.sort(reverse=True)
  for i in range(k):
    if a[i] < b[i]:
      a[i], b[i] = b[i], a[i]
    else:
      break

  print(sum(a))
  ```
