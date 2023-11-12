import sys
input = sys.stdin.readline

def dfs(i, sign, ret):
    global k 

    if len(ret) == k+1 or sign == k:
        rets.append(ret)
        return

    if signs[sign] == '<':
        can = list(filter(lambda x: x > i, nums))
    else:
        can = list(filter(lambda x: x < i, nums))

    for i in can:
        if str(i) not in list(ret):
            ret += str(i)
            dfs(i, sign+1, ret)
            ret = ret[:-1]

def solution():
    for i in nums:
        dfs(i, 0, str(i))

if __name__=='__main__':
    k = int(input())
    signs = input().rstrip().split()
    nums = [i for i in range(10)]

    rets = list()

    solution()

    print(rets[-1])
    print(rets[0])
