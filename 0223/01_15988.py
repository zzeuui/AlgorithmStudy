"""
python3으로는 안되고, pypy3으로 됨
"""
import sys
input = sys.stdin.readline

if __name__=='__main__':
    dp = [False]*(1000000+1)
    dp[1:4] = [1, 2, 4]
    for _ in range(int(input())):
        n = int(input())
        for i in range(4, n+1):
            if not dp[i]:
                dp[i] = (dp[i-1]+dp[i-2]+dp[i-3])%1000000009
            else:
                pass

        print(dp[n])

"""
케이스마다 모든 dp를 탐색하지 않도록 보완한 코드
그리고 어차피 리스트의 뒤에서부터 접근하면 되니깐 연산할 필요없음(i-3,i-2,i-1)
"""
dp = [1, 2, 4, 7]
for _ in range(int(input())):
    n = int(input())
    for i in range(len(dp), n):
        dp.append((dp[-3]+dp[-2]+dp[-1])%1000000009)
    print(dp[n-1])
