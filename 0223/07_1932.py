import sys
input = sys.stdin.readline

if __name__=='__main__':
    n = int(input())
    tri = list()
    dp = [0]*n
    for _ in range(n):
        tri.append(list(map(int, input().rstrip().split())))

    for t in tri:
        temp = [d for d in dp]
        for i in range(len(t)):
            dp[i] = max(temp[i-1]+t[i] if i > 0 else 0, temp[i]+t[i])

    print(max(dp))


