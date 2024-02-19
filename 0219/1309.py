""""
현재 칸이 추가되었을 사자를 두는 세가지 방법
1. 현재 왼쪽에 사자를 둘 경우 = 이전 칸 없음 + 이전 칸의 오른쪽만 있음
2. 현재 오른쪽에 사자를 둘 경우 = 이전 칸 없음 + 이전 칸의 왼쪽만 있음
3. 현재 칸에 사자를 두지 않을 경우 = 이전 칸 없음 + 이전 칸 오른쪽만 있음 + 이전 칸 왼쪽만 있음

dp[0] = [1, 1, 1] # n=1, 없거나(1) + 왼쪽에 두거나(1) + 오른쪽에 두거나(1) 
dp[1] = [3, 2, 2] # n=2, (1+1+1) + (1+1) + (1+1)
dp[2] = [7, 5, 5] # n=3, (3+2+2) + (3+2) + (2+2)
....
dp[n] = [dp[n-1][0]+dp[n-1][1]+dp[n-1][2],
         dp[n-1][0]+dp[n-1][2],
         dp[n-1][0]+dp[n-1][1]]

1. 현재 칸에 사자를 두지 않는 경우인,
   dp[n][0]은 dp[n-1][0]+dp[n-1][1]+dp[n-1][2]는
   결국, dp[n-1]를 모두 더한 값임을 알 수 있음


2. 현재 오른쪽과 왼쪽을 구하기 위해서는, 이전의 없는 칸과  반대칸을 더한 값이어야하는데
   반대칸은,
   이전의 모두 더한 값-또 그전의 모두 더한 값 = 이전의 오른쪽과 왼쪽 값 = a
   a/2 = 이전의 오른쪽 또는 왼쪽 값
   (이전의 반대칸값 + 이전의 모두 더한 값)*2 .. 왼쪽과 오른쪽이니깐 *2

   dp[n]을 dp[n]의 요소를 모두 더한 값이라고 할때,

   ((dp[n-1]-dp[n-2])/2) + dp[n-2])*2

3. dp[n] = dp[n-1] + ((dp[n-1]-dp[n-2])/2) + dp[n-2])*2이고,
   이를 정리하면, dp[n] = 2*dp[n-1] + dp[n-2]

   dp[n-1] = a, dp[n-2] = b..
   a + ((a-b)/2 + b)*2 = a + 2*(a-b)/2 + 2b = a + a - b + 2b = 2a-b+2b = 2a+b 
"""

n = int(input())

if n == 1:
    print(3)
else:
    dp = [1 for _ in range(n+1)]
    dp[1], dp[2] = 3, 7
    for i in range(3, n+1):
        dp[i] = (2*dp[i-1] + dp[i-2]) % 9901

    print(dp[n])
