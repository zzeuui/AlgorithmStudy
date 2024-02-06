import sys
input = sys.stdin.readline

if __name__=='__main__':
    n = int(input())
    if n == 1:
        pass
    else:
        d = 2
        while n != 1:
            if n%d == 0:
                print(d)
                n = n//d
            else:
                d += 1
