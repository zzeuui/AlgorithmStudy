"""
정답 23분 (50분)
"""

import sys
input = sys.stdin.readline

if __name__=='__main__':
    g = int(input())
    p = int(input())

    parent = [i for i in range(g+1)]
    for _ in range(p):
        flag = False

        #find parent from g_i to root
        for i in range(int(input())+1)[::-1]:
            if parent[i] != 0:
                parent[i] = 0
                flag = True
                break

        if not flag:
            break

    parent = [x for x in parent if x == 0]
    print(len(parent)-1)
