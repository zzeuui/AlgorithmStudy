# 06 무식하게 풀기(완전탐색 및 재귀호출)
완전탐색
- 문제가 주어졌을 때, 모든 경우의 수를 탐색하는 경우
- 탐색의 방법이 동일한 경우(큰 문제를 작은 문제로 나눌 수 있을 때)  

재귀호출
- 중첩되어 반복적으로 사용되는 코드 --> for문 대신 재귀호출 형태로 변경
- 기저사례 설정이 중요함. 기저사례를 적절히 설정함으로써, 모든 경우를 탐색하지않고 재귀호출을 더 빨리 중단할 수 있음.

## boggle.py
문제정의  
- 알파벳으로 채워진 보드판과 단어가 주어졌을 때, 단어가 보드판 안에서 한 줄로 이어질 수 있는 지 판단  

알고리즘
- 재귀호출 설정
  - 한 줄로 이어지는 판단하기 위해 선택된 알파벳을 중심으로 주변의 알파벳을 반복적으로 탐색하게 됨.
- 기저사례 설정
  - 탐색 도중 주변에 단어에 포함되는 알파벳이 없거나 이미 모두 탐색하여, 더이상 탐색할 알파벳이 없는 경우.
  ```
  ...
  start_inds = set(np.where(board_f > 0)[0])
  start_ind = list(start_inds - set(np.where(start_f > 0)[0]))
  if len(start_ind) > 0:
    start_ind = start_ind[0]
  else:
    return 1
  ...
  ```
  - 보드판의 모든 알파벳을 탐색한 경우
  ```
  if np.where(board_f == 0)[0].shape[0] == 0: return 1
  ```
- 기저사례에 의해 탐색이 중단되었을 때, 주어진 단어의 모든 알파벳을 찾으면 True, 아니면 False를 출력함
  ```
  print(len(word_f) == sum(word_f.values()))
  ```

비고
- 아마 동적계획법으로 코드를 작성함

## picnic.py
문제정의
- 친구인 학생들끼리 쌍을 만들었을 때, 나올수 있는 경우의 수 구하기

알고리즘 
- 재귀호출 설정
  - 경우의 수 중, 중복되는 쌍이 존재하게됨. 중복되는 쌍을 반복적으로 구하지 않고 재귀호출을 사용해 한 번만 계산함
  - example
    ```
    학생: 0, 1, 2, 3, 4, 5
    친구: (0, 1), (0, 2), (1, 2), (2, 3), (2, 4), (3, 5), (3, 4), (4, 5)
    None --> (0, 1) --> (0, 1), (2, 3) --> (0, 1), (2, 3), (4, 5)
    ```
- 기저사례 설정 
  - 가능한 쌍을 모두 만들었을 때, 쌍의 수가 학생수/2가 아닐 때 재귀호출 중단
  ```
  if len(cases) != students_n:
    return
  else:
    self.cases = cases
    self.NUM += 1
  ```
- 기저사례에 의해 탐색이 중단되었을 때, 중복되는 쌍에 대해서 전부 구해보고 종료함.
  ```
  while True:
    while True:
      picnic = Picnic(cases_eve)
      picnic.make_case(pairs_c, students_n, i_j)
               
   pairs = pairs[2:]
   if len(set(pairs)) != students_n: break;

   cases_eve = [pairs[0], pairs[1]]
   i_j = [-1, -1]
   pairs_c = pairs[2:].copy()
   
  ```

## boardcover.py
문제정의
- 보드판을 3타일로 구성된 기억자 모양으로 채움.  

알고리즘 
- 재귀호출 설정
  - 보드판을 채우는 방식이 여러개가 있고, 타일을 채울 때마다 방식을 달리할 수 있는 분기점이 존재함.
  여러 방식의 존재를 탐색하기 위해 처음부터 탐색하는 게 아니라, 각 분기점부터 보드판을 채울 수 있는지 탐색
- 기저사례 설정
  - 타일로 보드판을 모두 채움
  ```
  #self.total: number of tiles on the board
  if sum(board)== self.total:
    self.num += 1
    return 1
  ```
  - 타일로 보드판을 더 이상 채울 수 없어, 보드판의 변화가 없을 때
  ```
  if board_temp == board:
    return 0
  ```
- 기저사례에 의해 탐색이 중단되었을 때, 보드가 타일로 모두 채워진 경우(BoardCover.num)를 출력함
  ```
  if len(board)-sum(board)%3 == 0:
    bc = BoardCover(h, w)
    done = bc.cover(board)
    print(bc.num)
  else:
    print(0)
  ```

비고
- 1D 배열로 바꾸어서 코드 작성

## clocksync.py

문제정의
- 시계와 각 시계와 연결된 스위치가 존재. 스위치는 두 개 이상의 시계와 연결됨. 스위치를 누르면 시계는 3시간씩 추가됨(12h).
  이때 시계가 서로 다른 시간으로 설정되어있을 때, 모든 시계가 12시가 되도록 하는 최소한의 스위치를 누르는 횟수를 구해야함.

알고리즘
- 재귀호출 설정 
  - 모든 스위치를 순서대로 누르기 위해 재귀호출 사용. 재귀호출을 할 때, * 1번 스위치에서 2번 스위치로 바꾸는 식
  ```
  def solve(clocks, switch, cnt):
    solve(clocks, switch+1, cnt)
    
  solve(clocks, 0, 0)
  ```
- 기저사례 설정
  - 마지막 스위치에 도달함
  ```
  #linked: 시계와 스위치의 연결 관계가 저장된 데이터
  if switch == len(linked): return 0
  ```
- 기저사례에 의해 탐색이 중단되었을 때, 탐색한 횟수를 출력

비고
- 책 풀이를 완전히 참고함함
