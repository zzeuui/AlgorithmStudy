import sys
input = sys.stdin.readline

if __name__=='__main__':

    MAX = 1000000

    dp = [1]*(MAX+1)
    for i in range(2, MAX+1):
        j = 1
        while i*j < MAX+1:
            dp[i*j] += i
            j += 1

    s = [0]*(MAX+1)
    for i in range(1, MAX+1):
        s[i] = s[i-1] + dp[i]

    for _ in range(int(input())):
        print(s[int(input())])
