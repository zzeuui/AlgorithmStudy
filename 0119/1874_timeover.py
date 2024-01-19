import sys
input = sys.stdin.readline

if __name__=='__main__':
    target = [int(input().rstrip()) for _ in range(int(input().rstrip()))]

    nums = [i for i in range(1, len(target)+1)]
    stack = list()
    ret = ''

    for t in target:
        if t in stack:
            stack.pop()
            ret += '-\n'

        else:
            while True and nums:
                n = nums.pop(0)
                if n == t:
                    ret += '+\n-\n'
                    break
                else:
                    stack.append(n)
                    ret += '+\n'

    if not stack:
        print(ret.rstrip())
    else:
        print("NO")

