import math

RECUR_SIZE = 100

def decomposition_sum(m, i, n, min_ret):

    if n == 0 or n%RECUR_SIZE == 0 and n != i:
        return min_ret
    else:
        ns = list(map(int, str(n)))
        ret = n + sum(ns)

        n_place = list(set(ns))

        if len(n_place) == 1 and n_place[0] == 9 and ret < m:
            return min_ret

        if ret == m and n < min_ret:
            min_ret = n

        min_ret = decomposition_sum(m, i, n-1, min_ret)

        return min_ret

if __name__=='__main__':

    m = int(input())

    ret = m

    rec = math.ceil(m/RECUR_SIZE)

    done = 1

    for i in range(1, rec+1):

        i = min(i*RECUR_SIZE, m)
        
        min_ret = decomposition_sum(m, i, i, ret)

        ret = min(min_ret, ret)

    if ret == m:
        print(0)
    else:
        print(ret)
        
