import sys
input = sys.stdin.readline

if __name__=='__main__':
    for _ in range(int(input())):
        a, b = map(int, input().split())

        maxi = max(a, b)
        i = 1
        while True:
            if (maxi*i)%a == 0 and (maxi*i)%b == 0:
                maxi *= i
                break
            i += 1

        print(maxi)
