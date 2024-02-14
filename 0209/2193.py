"""
10844번 문제와 동일한 논리
"""
import sys
input = sys.stdin.readline

if __name__=='__main__':
    dp = [[0, 1]]

    for i in range(int(input())-1):
        dp.append([dp[i][0]+dp[i][1], dp[i][0]])

    print(sum(dp[-1]))
        
