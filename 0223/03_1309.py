import sys
input = sys.stdin.readline

if __name__=='__main__':
    n = int(input())
    dp = [[1, 2]]
    for i in range(1, n):
        no = (dp[-1][0] + dp[-1][1])%9901
        yes = (2*dp[-1][0] + dp[-1][1])%9901
        
        dp.append([no, yes])
        
    print(sum(dp[n-1])%9901)
