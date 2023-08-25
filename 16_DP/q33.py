"""
정답 1시간 18분 (30분)
dp로 안풀음
"""
import sys
input = sys.stdin.readline

def dfs(day, cur):
    global n, ret

    t, p = data[day]
    if day+t > n:
        if ret < cur:
            ret = cur
            
    elif day+t == n:
        if ret < cur+p:
            ret = cur+p

    cur += p
    for nt in range(day+t, n):
        dfs(nt, cur)

if __name__=='__main__':
    n = int(input())
    data = list()
    for i in range(n):
        t, p = map(int, input().rstrip().split())
        data.append((t, p))

    rets = []
    for i in range(n):
        ret = 0
        cur = 0
        dfs(i, cur)
        rets.append(ret)

    print(max(rets))

"""
책 풀이

**뒤 쪽부터 거꾸로 확인하는 방식으로 접근**

현재 상담 일자의 이윤(p[i]) + 현재 상담을 마친 일자부터의 최대 이윤(dp[t[i]+i])
dp[i] = i번째 날부터 마지막 날까지 낼 수 있는 최대 이익
dp[i] = max(p[i]+dp[t[i]+i], max_value)
"""
n = int(input())
t = []
p = []
dp = [0]*(n+1)
max_value = 0

for _ in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)

for i in range(n-1, -1, -1):
    time = t[i]+i
    if time <= n:
        dp[i] = max(p[i]+dp[time], max_value)
        max_value = dp[i]
    else:
        dp[i] = max_value

print(max_value)
