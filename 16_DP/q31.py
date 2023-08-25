"""

정답 44분 (30분)

왜 문제 이해만 25분 걸림..

"""
import sys
input = sys.stdin.readline

def solution(n, m, nums):
    direction = [(-1, -1), (0, -1), (1, -1)]

    ret = [[0]*m for _ in range(n)]

    for i in range(n):
        ret[i][0] = nums[i][0]
    
    for j in range(1, m):
        for i in range(n):
            now = nums[i][j]
            for dx, dy in direction:
                prex, prey = i+dx, j+dy
                if 0<= prex < n and 0<= prey < m:
                    ret[i][j] = max(ret[i][j], now+ret[prex][prey])

    return max(sum(ret, [])) 

if __name__=='__main__':
    for _ in range(int(input())):
        n, m = map(int, input().rstrip().split())
        nums = list(map(int, input().rstrip().split()))
        nums = [nums[i:i+m] for i in range(0, n*m, m)]

        print(solution(n, m, nums))

"""
책 풀이
인덱싱과 비교를 더 간단하게 구현함
마지막 열의 수만 비교하면 됨
"""
for tc in range(int(input())):
    n, m = map(int, input().split())
    array = list(map(int, input().split()))

    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index:inde+m])
        index += m

    for j in range(1, m):
        for i in range(n):
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i-1][j-1]

            if i == n-1:
                left_down = 0
            else:
                left_down = dp[i+1][j-1]

            left = dp[i][j-1]
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)

    result = 0
    for i in range(n):
        result = max(result, dp[i][m-1])

    print(result)