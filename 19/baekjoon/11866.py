
if __name__=='__main__':
    n, k = map(int, input().split())

    j=0
    p = [i for i in range(1, n+1)]
    t = list()
    while p:
        j = (j+k-1) % len(p)
        t.append(p.pop(j))

    print(str(t).replace('[', '<').replace(']', '>'))

