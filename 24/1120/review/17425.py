import sys
input = sys.stdin.readline

def sum_of_divisor():
    global MAX

    dp = [1]*(MAX+1)
    for i in range(2, MAX+1):
        j = 1
        while i*j <= MAX:
            dp[i*j] += i
            j += 1

    s = [0]*(MAX+1)
    for i in range(1, MAX+1):
        s[i] = s[i-1] + dp[i]

    return s

if __name__=='__main__':

    MAX = 1000000

    s = sum_of_divisor()

    for _ in range(int(input())):
        n = int(input())
        print(s[n])
