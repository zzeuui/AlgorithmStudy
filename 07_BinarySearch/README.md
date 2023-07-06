# 07 이진탐색

## 1) 범위를 반씩 좁혀가는 탐색
#### 순차 탐색(Sequential Search)
- 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례대로 확인하는 방법
- $O(N)$
```
for i range(len(array)):
  if array[i] == target:
    return i+1 #순서 반환

or

ind = list.index(target)
```

#### 이진 탐색(Binary Search)
- 데이터가 정렬되어 있어야만 사용할 수 있고, 탐색 범위를 절반씩 좁혀가며 데이터를 탐색
- $O(logN)$
- 찾으려는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교
  - 탐색하고자 하는 범위의 시작점, 끝점, 중간점 설정
  - 중간점과 찾으려는 데이터를 비교하여 중간점이 더 크다면, 끝점을 중간점 앞으로 위치
  - 데이터와 비교해 더 작으면, 시작점을 중간점 뒤로 위치
  - 시작점 혹은 끝점이 중간점 위치와 동일하다면 종료
```
# recursive
def binary_search(target, start, end):
  if start > end:
    return None
  
  mid = (start+end) // 2
  if array[mid] == target:
    return mid
  elif array[mid] > target:
    return binary_search(target, start, mid-1)
  else:
    return binary_search(target, mid+1, end)

array = list()
binary_search(target, 0, len(array)-1)

# iterative
ind = None
while start <= end:
  mid = (start+end) // 2
  if array[mid] == target:
    ind = mid
    break
  elif array[mid] > target:
    end = mid-1
  else:
    start = mid + 1
```

#### 트리 자료구조
- 노드와 간선으로 구성된 자료구조. 노드는 정보의 단위이고, 노드와 노드가 간선으로 연결되어 있다고 표현됨
- 트리 자료구조의 주요 특징
  - 트리는 부모 노드와 자식 노드의 관계로 표현된다
  - 트리의 최상단 노드를 루트 노드라고 한다
  - 트리의 최하단 노드를 단말 노드라고 한다
  - 트리에서 일부를 떼어내도 트리 구조이며 이를 서브 트리라 한다
  - 트리는 파일 시스템과 같이 계층적이고 정렬된 데이터를 다루기에 적합하다

#### 이진 탐색 트리
- 이진 트리
  - 모든 노드가 둘 이하의 자식 노드를 가짐
  - 부모 노드보다 왼쪽 자식 노드가 작고, 부모 노드보다 오른쪽 자식 노드가 크다
- 이진 트리 탐색
  - 현재 노드가 찾는 값보다 작다면 왼쪽 자식 노드 방문, 크다면 오른쪽 자식 노드 방문
- 이진 트리 자료구조 구현 문제는 출제 빈도가 낮음..

#### 빠르게 입력받기
- sys 라이브러리 사용
```
import sys
input_data = sys.stdin.readline().rstrip()
print(input_data)

input = sys.stdin.readline
print(input().rstrip())
```

## 2) 부품 찾기
- 문제
  - N개의 부품이 있을 때, 특정한 M개의 부품이 있는 지 확인
- 풀이
  - 이진 탐색으로 해결 $O((N+M)*logN)$, 29분
  ```
  import sys
  input = sys.stdin.readline
  n = int(input().rstrip())
  ns = list(map(int, input().rstrip().split()))
  m = int(input().rstrip())
  ms = list(map(int, input().rstrip().split()))

  def binary_search(t, start, end):
    if start > end:
      return False
    mid = (strat+end) //2
    if ns[mid] == t: return True
    elif ns[mid] > t: return binary_search(t, start, mid-1)
    else: return binary_search(t, mid+1, end)

  for t in ms:
    if binary_earch(t, 0, n-1): print('yes', end=' ')
    else: print('no', end=' ')
  ```
  - 계수 정렬
  ```
  array = [0]*1000001
  for i in ns:
    array[i] = 1
  for j in ms:
    if array[j] == 1:
      print('yes', end=' ')
    else:
      print('no', end=' ')
  ```
  - 집합 자료형
  ```
  ns = set(ns)
  for i in ms:
    if i in ns:
      print('yes', end=' ')
    else:
      print('no', end=' ')
    
  ```

## 3) 떡볶이 떡 만들기
- 문제
  - 높이(H)만큼 한번에 여러떡을 절단할 수 있고, 손님에게 잘린떡을 제공. 높이보다 낮은 떡은 잘리지 않음
  - ex) 절다기 높이를 15로 설정. 떡은 각각 19, 14, 10, 17 일 때, 손님에게 잘린떡 4+0+0+2 = 6을 제공
  - 손님이 적어도 M길이 만큼의 떡을 얻기 위해 설정해야할 절단기 높이의 최댓값
- 풀이
  - 높이가 주어졌을 때 나온 값과 t를 비교하여 이진 탐색, 28분
  ```
  import sys
  input = sys.stdin.readline
 
  
  def compute_length(h):
    # 1
    return sum([0 if c < h else c-h for c in rice_cake])
    
    # 2 in book
    total = 0
    for c in rice_cake:
      if x > h: total += c-h
    return total

  def binary_search(t, start, end):
    if start > end:
      return end
    mid = (start+end) // 2
    cut_length = compute_length(mid)
    if cut_length == t: return mid
    elif cut_length > t: return binary_search(t, mid+1, end)
    else: binary_search(t, start, mid-1)

  n, m = map(int, input().rstrip().split())
  rice_cake = list(map(int, input().rstrip().split()))

  print(binary_search(m, 0, max(rice_cake)))
  ```
