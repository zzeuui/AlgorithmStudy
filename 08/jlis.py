n, m = 0, 0
a, b = list(), list()
cache, ab_f = list(), list()

def jlis(ind_a, ind_b):

    ret = cache[ind_a][ind_b]
    if ret != -1: return ret
    
    ret = 2
    a_ele = a[ind_a]
    b_ele = b[ind_b]
    ab_f[a_ele] = 1
    ab_f[b_ele] = 1

    max_ele = min(a_ele, b_ele)

    for next_a in range(ind_a+1, n):
        if max_ele < a[next_a] and ab_f[a[next_a]] != 1:
            ret = max(ret, jlis(next_a, ind_b)+1)
    for next_b in range(ind_b+1, m):
        if max_ele < b[next_b] and ab_f[b[next_b]] != 1:
            ret = max(ret, jlis(ind_a, next_b)+1)

    cache[ind_a][ind_b] = ret

    return ret

if __name__=='__main__':
    case_n = int(input())

    for _ in range(case_n):
        n_m = list(map(int, input().split(' ')))
        n = n_m[0]
        m = n_m[1]
        a = list(map(int, input().split(' ')))
        b = list(map(int, input().split(' ')))

        max_len = 0
        for i in range(n):
            for j in range(m):
                cache = [[-1]*m]*n
                ab_f = [0]*(max(a+b)+1)
                jlis_len = jlis(i, j)
                max_len = max(max_len, jlis_len)

        print(f'max_len: {max_len}')
