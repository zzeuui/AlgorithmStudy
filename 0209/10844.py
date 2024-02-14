"""
1계단식 증가하는 수는..
이전 자릿수의 끝자리의 앞 뒤의 수를 붙여서 만들 수 있음
ex) 12 -> 1 or 3 -> 121, 123
이를 규칙으로 dp를 사용해 계산함
"""
import sys
input = sys.stdin.readline

if __name__=='__main__':
    dp = [[1 for _ in range(10)]]
    dp[0][0] = 0

    for i in range(int(input())-1):
        temp = [0]*10

        temp[0] = dp[i][1]
        for j in range(1, 9):
            temp[j] = dp[i][j-1] + dp[i][j+1]
        temp[9] = dp[i][8]

        dp.append(temp)

    print(sum(dp[-1])%1000000000)
