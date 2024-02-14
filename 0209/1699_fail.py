import sys
input = sys.stdin.readline

if __name__=='__main__':
    n = int(input())
    
    dp = [float('inf') for _ in range(n+1)]
    dp[n] = 0

    """
    for i in range(int(n**0.5), 0, -1):
        dp[n%(i**2)] = min(dp[n%(i**2)], dp[n]+n//(i**2))

    for m in range(n, 0, -1):
        if dp[m] != float('inf'):
            for i in range(int(m**0.5), 0, -1):
                dp[m%(i**2)] = min(dp[m%(i**2)], dp[m]+m//(i**2))

    for m in range(n, 0, -1):
        for i in range(int(m**0.5), 0, -1):
            nt = m%(i**2)
            dp[nt] = min(dp[nt], dp[m]+m//(i**2))
    """

    valid = [n]
    while valid:
        m = valid.pop()
        for i in range(int(m**0.5), 0, -1):
            nt = m%(i**2)
            if dp[nt] == float('inf'): 
                valid.append(nt)
            dp[nt] = min(dp[nt], dp[m]+m//(i**2))

    print(dp[0])
