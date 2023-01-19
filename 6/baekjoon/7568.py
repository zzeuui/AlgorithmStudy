import itertools

if __name__=='__main__':
    n = int(input())

    people = list()
    for i in range(n):
        people.append({i: list(map(int, input().split(' ')))})

    rank = [1 for _ in range(n)]
    com_peo = list(itertools.combinations(people, 2))

    for c in com_peo:
        p1 = list(c[0].items())[0]
        p2 = list(c[1].items())[0]

        if p1[1][0] > p2[1][0] and p1[1][1] > p2[1][1]:
            rank[p2[0]] += 1
        elif p1[1][0] < p2[1][0] and p1[1][1] < p2[1][1]:
            rank[p1[0]] += 1

    print(" ".join(list(map(str, (rank)))))

