import sys
input = sys.stdin.readline

if __name__=='__main__':
    a, b = map(int, input().rstrip().split())
    m = int(input())
    nums = list(map(int, input().rstrip().split()))

    de = 0
    for n in nums:
        de *= a
        de += n

    ret = list()
    while de != 0:
        ret.append(de%b)
        de = de//b

    print(*ret[::-1])
