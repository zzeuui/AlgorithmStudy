"""
타일, 동물원, RGB등 상황이 주어졌을 때 분기점(경우)을 dp로 구현하는 것 같다.
한 시점의 분기점(경우)를 표현하기 위해 이중 리스트를 사용하고.. 
dp[0][0]: 첫번째 상황에서 첫번째 경우
dp[n][n]: T=n일 때, n번째 경우
"""
import sys
input = sys.stdin.readline

if __name__=='__main__':
    n = int(input())
    house = list()
    for _ in range(n):
        house.append(list(map(int, input().rstrip().split())))

    dp = [h for h in house]
    for i in range(1, n):
        dp[i][0] = min(dp[i][0]+dp[i-1][1], dp[i][0]+dp[i-1][2])
        dp[i][1] = min(dp[i][1]+dp[i-1][0], dp[i][1]+dp[i-1][2])
        dp[i][2] = min(dp[i][2]+dp[i-1][0], dp[i][2]+dp[i-1][1])

    print(min(dp[-1]))
