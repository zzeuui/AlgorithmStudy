import sys
input = sys.stdin.readline

if __name__=='__main__':

    MAX = 1000000
    s = [1]*(MAX+1)

    for i in range(2, MAX+1):
        j = 1
        while i*j < MAX+1:
            s[i*j] += i
            j += 1

    d = [0]*(MAX+1)
    for i in range(1, MAX+1):
        d[i] = d[i-1]+s[i]

    for _ in range(int(input())):
        print(d[int(input())])
