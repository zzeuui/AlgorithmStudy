import sys
input = sys.stdin.readline

if __name__=='__main__':
    n = int(input())
    digit = len(str(n))

    ret = 0
    for i in range(digit-1):
        ret += 9*(10**i)*(i+1)

    ret += (n-(10**(digit-1))+1)*digit

    print(ret)
