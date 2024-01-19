import sys
input = sys.stdin.readline

def permutations(s, ret):

    if len(ret) == 6:
        print(' '.join(list(map(str, ret))))

    for n in s:
        if n not in ret and n > ret[-1]:
            ret.append(n)
            permutations(s, ret)
            ret.pop(-1)

if __name__=='__main__':
    
    while True:
        nums = list(map(int, input().rstrip().split()))
        k = nums[0]
        s = nums[1:]

        if k == 0: break

        for n in s:
            permutations(s, [n])

        print()
