import sys
input = sys.stdin.readline

if __name__=='__main__':
    n, b = input().rstrip().split()
    n = [int(i) if ord(i) <= ord('9') else ord(i)-55 for i in n]
    b = int(b)

    ret = 0
    for i in n:
        ret *= b
        ret += i
    print(ret)
