# 08 동적 계획법

## 동적 계획법

개념
- 중복되는 부분문제(overlapping subproblems)에 대한 계산 결과를 캐시(cache)에 저장하여,
그 결과를 재활용함으로써 속도를 향상시키는 방법.

목적
- 나눠진 문제들이 같은 부분문제에 의존하는 경우, 단순한 재귀호출로 해결하면 중복계산이 많아지며
계산의 중복 횟수가 분할할 수록 지수적으로 증가하는 조합 폭발(combinatorial explosion)이 야기된다.
동적 계획법은 조합 폭발을 해결하기 위해 고안된 알고리즘 설계 기법이다.

대표예
- 이항계수(binomial coefficient)
  - n개의 서로 다른 원소 중에서 r개의 원소를 순서없이 골라내는 조합의 가짓수
  ```
  int bino(int n, int r){
    //기저 사례: n=r(모든 원소를 다 고르는 경우) 혹은 r=0 (고를 원소가 없는 경우)
    if(r==0 || n==r) return 1;
    return bino(n-1, r-1) + bino(n-1, r); //이항계수 점화식
  ```
  - 동적 계획법 적용
    - 이항계수의 점화식에 따라 중복되는 n, r 조합이 존재함 => n, r 조합에 대한 결과값을 저장 
  ```
  int cache[30][30];
  int bino2(int n, int r){
    //기저 사례
    if(r==0 || n==r) return 1;
    //-1이 아니라면 한 번 계산했던 값이니 곧장 반환
    if(cache[n][r] != -1) return cache[n][r];
    //직접 계산한 뒤 배열에 저장
    return cache[n][r] = bino2(n-1, r-1) + bino2(n-1, r);
  }
  ```
  
## 메모이제이션

개념
- 한 번 계산한 값을 저장했다가 재활용하는 최적화 기법
- 참조적 투명 함수의 경우에만 적용할 수 있음
  - 참조적 투명 함수(referential transparency): 함수의 반환 값이 그 입력 값만으로 결정되는지의 여부

구현
1. 기저사례 먼저 처리
2. 함수의 반환 값과 다른 값으로 캐시를 초기화  

   c++의 경우  

3. 함수 내에서 캐시 접근에 대해 참조형 변수를 사용하여 값이 자동으로 바뀌도록 함  
    ```
    type& var = cache[i]
    ```
 4. 배열을 초기화하는 memset() 사용
    ```
    int cache[10]
    int main(){
      memset(cache, -1, sizeof(cache))
    }
    ```

시간복잡도
- (존재하는 부분 문제의 수)*(한 부분 문제를 풀 때 필요한 반복문의 수행 횟수)

## 예제: 외발 뛰기 (문제 ID: JUMPGAME, 난이도: 하)

문제
- NxN 크기의 격자에 1부터 9까지의 정수를 쓴 게임판
- 각 칸에 적혀 있는 숫자만큼 아래쪽이나 오른쪽으로 이동 가능
- 왼쪽 위 칸에서 시작해서 게임판의 오른쪽 아래칸에 도착할 수 있는지 여부 판단(true / false 문제)

재귀 호출
```
int n, board[100][100];
bool jump(int y, int x){
  int jumpSize = board[y][x];
  return jump(y+jumpSize, x) || jump(y, x+jumpSize)
}
```
동적 계획법
#### 입력의 개수가 n*n으로 제한됨 
```
int n, board[100][100];
int cache[100][100];
bool jump2(int y, int x){
  int& ret = cache[y][x];
  if(ret != -1) return ret;
  int jumpSize = board[y][x];
  return ret = jump(y+jumpSize, x) || jump(y, x+jumpSize)
}
```

동적계획법 레시피
- 주어진 문제를 완전 탐색으로 해결
- 중복된 부분 문제를 한 번만 계산하도록 
