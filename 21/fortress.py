'''
1
8
21 15 20
15 15 10
13 12 5
12 12 3
19 19 2
30 24 5
32 10 7
32 9 4
'''

from collections import defaultdict

def contains(i, j):
    x1, y1, r1 = walls[i] #larger one
    x2, y2, r2 = walls[j] 
    
    # the difference between the two centers
    # is less than the radius of larger one
    return (x1-x2)**2 + (y1-y2)**2 < r1**2 

def height(root):

    # handling the root do not have children 
    if root not in children:
        return 0

    # Starting from the root, add the height
    # recursively up to the children of the root.
    heights = [1+height(c) for c in children[root]]
    heights.sort()

    if len(heights) >= 2:
        global best
        best = max(best, heights[-1]+heights[-2])
    return heights[-1]


for case in range(int(input())):
    N = int(input())
    walls = [tuple(map(int, input().split())) for _ in range(N)]
    walls.sort(key=lambda x: x[2])

    children = defaultdict(list)

    for i in range(N-1):
        for j in range(i+1, N):
            if contains(j, i):
                children[j].append(i)
                break

    root = N-1
    best = 0
    h = height(root)
    print(max(best, h))
