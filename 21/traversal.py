"""
#incorrect
#1. when deciding root, pop it from list
#2. according to preorder traverse, all root can be traversed in sequence.
#3. info of preorder traverse is important only to get root
#4. using inorder traverse for split to left and right
#5. just print root, cuz traverse in sequence with recursive function 

order = [1, 2, 0]

def split_tree(frt, mid, bak):
    root = frt[0]
    tree = [root, [], []]
    sub = [[], []]
    sub[0] = mid[:mid.index(root)]
    sub[1] = mid[mid.index(root)+1:]
    
    for e in frt[1:]: 
        if e in sub[0]: tree[1].append(e)
        else: tree[2].append(e)

    for i in range(1, 3):
        if len(tree[i]) > 1:
            tree[i], bak = split_tree(tree[i], sub[i-1], bak)

    for i in order:

        if i == 0:
            bak.append(tree[i])
        elif len(tree[i]) == 1:
            bak.append(tree[i][0])

    return tree, bak

if __name__=='__main__':

    for _ in range(int(input())):

        n = int(input())

        frt = list(map(str, input().split(' ')))
        mid = list(map(str, input().split(' ')))

        bak = list()
        _, bak = split_tree(frt, mid, bak)
        print(' '.join(bak))
"""

def split_tree(frt, mid):

    if not mid:
        return

    root = frt.pop(0)
    split_tree(frt, mid[:mid.index(root)])
    split_tree(frt, mid[mid.index(root)+1:])

    print(root, end=' ')

if __name__=='__main__':

    for _ in range(int(input())):

        n = int(input())

        frt = list(map(str, input().split(' ')))
        mid = list(map(str, input().split(' ')))

        split_tree(frt, mid)
