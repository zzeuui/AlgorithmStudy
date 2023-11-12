import sys
input = sys.stdin.readline

if __name__=='__main__':
    n = int(input())
    T, P = [0]*(n+1), [0]*(n+1)

    for i in range(1, n+1):
        t, p = map(int, input().rstrip().split())
        T[i], P[i] = t, p

    dp = [0]*(n+1)

    for i in range(1, n+1):

        st = i

        nt = T[st] + st
        if nt <= n+1:
            dp[st] = max(dp[st], P[st])
            for j in range(nt, n+1):
                if j+T[j] <= n+1:
                    dp[j] = max(dp[j], P[j] + dp[st])

    print(max(dp))
