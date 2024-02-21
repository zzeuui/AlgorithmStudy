"""
1108ms..
"""
import sys
input = sys.stdin.readline

if __name__=='__main__':
    for _ in range(int(input())):
        n = int(input())
        sticker = list()
        for _ in range(2):
            sticker.append([0]+list(map(int, input().rstrip().split())))

        dp = [[0]*2 for _ in range(n+1)]
        dp[1] = [sticker[0][1], sticker[1][1]]
        for i in range(2, n+1):
            #위쪽을 선택할 수 있는 경우
            dp[i][0] = sticker[0][i]+max(dp[i-1][1], dp[i-2][0], dp[i-2][1])
            #아래쪽을 선택할 수 있는 경우
            dp[i][1] = sticker[1][i]+max(dp[i-1][0], dp[i-2][0], dp[i-2][1])
            
        print(max(dp[-1]))
