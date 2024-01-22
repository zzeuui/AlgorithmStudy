import sys
input = sys.stdin.readline

if __name__=='__main__':
    line = list(input().rstrip())[::-1]
    stack = list()
    pre = ''

    ret = 0
    while line:
        l = line.pop()
        if l == '(':
            stack.append(l)
        else:
            stack.pop()
            if pre == '(': #laser
                ret += len(stack)
            else: #bar
                ret += 1

        pre = l
    
    print(ret)

