import sys
input = sys.stdin.readline

if __name__=='__main__':
    n = int(input())
    divisors = list(map(int, input().rstrip().split()))

    if n == 1:
        print(divisors[0]**2)

    else:
        divisors.sort()
        print(divisors[0]*divisors[-1])
