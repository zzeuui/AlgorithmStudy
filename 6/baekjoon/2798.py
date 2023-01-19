import itertools

def combinations_2(array, r):
    for i in range(len(array)):
        if r == 1: # 종료 조건
            yield [array[i]]
        else:
            for next in combinations_2(array[i+1:], r-1):
                yield [array[i]] + next

if __name__=='__main__':
    n_m = list(map(int, input().split(' ')))
    cards = list(map(int, input().split(' ')))

    combinations = list(itertools.combinations(cards, 3))

    sumations = sorted([sum(c) for c in combinations if sum(c) <= n_m[1]])

    print(sumations[-1])

