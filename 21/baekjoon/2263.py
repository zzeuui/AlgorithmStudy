"""
incorrect
def f(pos, poe, ins, ine):

    if not inod[ins:ine]: return

    root = postod[pos:poe][-1]

    print(root, end=' ')

    inod_ind = inod[ins:ine].index(root) +ins
    postod_ind = len(inod[ins:inod_ind]) + pos

    f(pos, postod_ind, ins, inod_ind)
    f(postod_ind, poe-1, inod_ind+1, ine)

if __name__=='__main__':
    n = int(input())
    inod = input().split()
    postod = input().split()

    f(0, n, 0, n)
"""
from collections import defaultdict
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

nodeNum = defaultdict(int)
#nodeNum = [0] * (n + 1)
for i in range(n):
    nodeNum[inorder[i]] = i

def preorder(inStart, inEnd, postStart, postEnd):
    if (inStart > inEnd) or (postStart > postEnd):
        return
                    
    root = postorder[postEnd]
            
    leftNode = nodeNum[root] - inStart #number of nodes on left subtree
    rightNode = inEnd - nodeNum[root] #number of nodes on right subtree
        
    print(root, end = " ")
    preorder(inStart, inStart + leftNode - 1, postStart, postStart + leftNode - 1)
    preorder(inEnd - rightNode + 1, inEnd, postEnd - rightNode, postEnd - 1)

preorder(0, n - 1, 0, n - 1)



