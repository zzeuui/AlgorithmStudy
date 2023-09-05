"""
오답 1시간 53분

부모 노드가 너 낮은 순위인 경우, 높은 부모 노드를 가진 노드의 부모 노드를 낮은 부모 노드로 바꾸고,
낮은 순위의 부모 노드의 랭킹과 높은 순위의 부모 노드의 랭킹을 바꾸는 ......

...

"""
import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        x = find_parent(parent, parent[x])

    return x

if __name__=='__main__':
    for _ in range(int(input())):
        n = int(input())
        teams = {x:i for i, x in enumerate(list(map(int, input().rstrip().split())))}
        m = int(input())
        chages = list()
        for _ in range(m):
            chages.append(list(map(int, input().rstrip().split())))

        parent = [i for i in range(n)]
        ranks = [i for i in range(n)]

        for chage in chages:
            a, b = teams[chage[0]], teams[chage[1]]
            ap = find_parent(parent, a)
            bp = find_parent(parent, b)

            print(f'{ap}, {bp}')
            if ap < bp:
                parent[a] = b
                ranks[a], ranks[bp] = ranks[bp], ranks[a]
            else:
                parent[b] = a
                ranks[b], ranks[ap] = ranks[ap], ranks[b]


        print(ranks)
        print(parent)

        ranks = [(x, i) for i, x in enumerate(ranks)]
        ranks.sort()

        keys = list(teams.keys())
        ret = ' '.join([str(keys[x[1]]) for x in ranks])
        print(ret)
