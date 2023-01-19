
if __name__=='__main__':

    m = int(input())

    ret = m

    for i in range(m, 0, -1):
        ns = list(map(int, str(i)))
        n = i + sum(ns)

        if n == m:
            ret = min(ret, i)

    if ret == m:
        print(0)
    else:
        print(ret)
        
