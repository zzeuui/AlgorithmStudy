from collections import defaultdict
"""
if __name__=='__main__':

    n = int(input())
    
    tree = defaultdict(list)
    p_c = {i+1: 0 for i in range(n)}
    c_f = [i+2 for i in range(n-1)]

    for _ in range(n-1):
        n1, n2 = map(int, input().split())
        tree[n1].append(n2)

        if n1 == 1: p_c[n2] = 1
        elif n2 == 1: p_c[n1] = 1
        else: tree[n1].append(n2)

    while True:
        for p, pp in p_c.items():
            if p in c_f and pp > 0:
                for n1, n2 in tree.items():
                    if n1 == p:
                        for n in n2:
                            if p_c[n] == 0:
                                p_c[n] = p
                    if p in n2:
                        if p_c[n1] == 0:
                            p_c[n1] = p
                    
                del c_f[c_f.index(p)]

        if not c_f:
            break

    del p_c[1]

    for k, i in p_c.items():
        print(i)

if __name__=='__main__':
    n = int(input())

    edge = list()
    tree = defaultdict(list)
    flag = list()
    for _ in range(n-1):
        n1, n2 = map(int, input().split())
        if n1 == 1: 
            tree[n2] = 1
            flag.append(n2)
        elif n2 == 1: 
            tree[n1] = 1
            flag.append(n1)
        else: edge.append([n1, n2])

    while edge:
        p, c = edge.pop() 

        if p in flag:
            tree[c] = p
            flag.append(c)
        elif c in flag:
            tree[p] = c
            flag.append(p)
        else:
            edge.insert(0, [p,c])

    tree = sorted(tree.items())
    for k, i in tree:
        print(i)
def F():
    for f in flag:
        if f in edge.keys():
            for c in edge[f]:
                tree[c] = f
                flag.append(c)
            del edge[f]

if __name__=='__main__':
    n = int(input())

    edge = defaultdict(list)
    tree = defaultdict(list)
    flag = list()
    for _ in range(n-1):
        n1, n2 = map(int, input().split())
        if n1 == 1: 
            tree[n2] = 1
            flag.append(n2)
        elif n2 == 1: 
            tree[n1] = 1
            flag.append(n1)
        else: edge[n1].append(n2)

    F()

    for f in flag:
        for k, i in edge.items():
            if f in i:
                tree[k] = f
                flag.append(k)
                del i[i.index(f)]
        edge = { k:i for k,i in edge.items() if i}

    F()

    tree = sorted(tree.items())
    for k, i in tree:
        print(i)

"""
# ref: https://velog.io/@dark6ro/%EB%B0%B1%EC%A4%80-11725%EB%B2%88-%ED%8A%B8%EB%A6%AC%EC%9D%98-%EB%B6%80%EB%AA%A8-%EC%B0%BE%EA%B8%B0
# BFS: Breadth-First Search

import sys
from collections import deque
input = sys.stdin.readline

def solution(N,tree):
	q = deque([1])
	parent = [0] * (N+1)
	while q:
		now = q.popleft()
		for i in tree[now]:
			if parent[i] == 0 and i != 1:
				parent[i] = now
				q.append(i)
	for i in range(2,N+1):
		print(parent[i])

if __name__ == "__main__":
	N = int(input())
	tree = dict()
	for i in range(1,N+1):
		tree[i] = []
	for _ in range(N-1):
		n1,n2 = map(int,input().split())
		tree[n1].append(n2)
		tree[n2].append(n1)
	solution(N,tree)
