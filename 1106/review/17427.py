if __name__=='__main__':
    n = int(input())

    ret = 0
    for i in range(1, n+1):
        ret += (n//i)*i

    print(ret)
