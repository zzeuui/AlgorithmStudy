cache = list()
arr = list()

def classify(a, b):
    m = arr[a:b]

    if len(list(set(m))) == 1: return 1

    progressive = True
    for i in range(len(m)-1):
        if m[i+1] - m[i] != m[1] - m[0]:
            progressive = False

    if progressive and abs(m[1] - m[0]) == 1:
        return 2

    alternating = True
    for i in range(len(m)):
        if m[i] != m[i%2]:
            alternating = False

    if alternating: return 4
    if progressive: return 5
    return 10

def memorize(begin):
    if(begin == len(arr)): return 0

    ret = cache[begin]
    if ret != -1: return ret

    ret = 30000 #10000/5*10 = 20000

    for l in range(3, 6):
        if begin+l <= len(arr):
            ret = min(ret, memorize(begin+l)+classify(begin, begin+l))

    cache[begin] = ret

    return ret

if __name__=='__main__':
    case_n = int(input())

    for _ in range(case_n):
        arr = list(map(int, list(input())))
        cache = [-1]*10002
        ret = memorize(0)
        print(ret)

