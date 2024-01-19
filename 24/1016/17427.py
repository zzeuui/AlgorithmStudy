import sys
input = sys.stdin.readline

if __name__=='__main__':
    n = int(input())

    divisor = list()
    for i in range(1, n+1):
        for d in range(1, i+1):
            if i%d == 0:
                divisor.append(d)

    print(sum(divisor))


    divisor = list()
    for d in range(1, 31):
        if 30%d == 0:
            divisor.append(d)

    print(divisor)
