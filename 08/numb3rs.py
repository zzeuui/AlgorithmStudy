from functools import lru_cache

@lru_cache(maxsize=None)
def search3(here, days):
    if days == 0:
        if here == p: return 1
        else: return 0

    return sum(search3(there, days-1)/deg[there] for there in range(n) if connected[here][there])

if __name__=='__main__':
    for _ in range(int(input())):
        n, d, p = map(int,input().split(' '))
        connected = [list(map(int, input().split(' '))) for _ in range(n)]
        deg = [sum(c) for c in connected]
        t = int(input())
        ts = list(map(int, input().split(' ')))

        for i in ts:
            print(search3(i, d), end=' ')


