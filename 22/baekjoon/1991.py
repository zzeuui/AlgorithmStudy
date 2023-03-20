#트리도 어차피 루트와 키값을 가지고 경로를 찾는 거니깐, 
#트리 구현을 위해 딕셔너리를 이용할 수 있음
#루트 - 딕셔너리 키, 키값 - 딕셔러니 값

def preorder(key):
    print(key, end='')
    if tree[key][0] != '.':
        preorder(tree[key][0])
    
    if tree[key][1] != '.':
        preorder(tree[key][1])

def inorder(key):
    if tree[key][0] != '.':
        inorder(tree[key][0])
    print(key, end='')
    if tree[key][1] !=  '.':
        inorder(tree[key][1])

def postorder(key):
    if tree[key][0] != '.':
        postorder(tree[key][0])
    if tree[key][1] !=  '.':
        postorder(tree[key][1])
    print(key, end='')

if __name__=='__main__':

    tree = {}

    for _ in range(int(input())):
        root, left, right = map(str, input().split())
        
        tree[root] = [left, right]

    preorder('A')
    print()
    inorder('A')
    print()
    postorder('A')
