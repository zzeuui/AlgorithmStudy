import sys
input = sys.stdin.readline

if __name__=='__main__':
    cnt = 1
    stack = list()
    #ret = list() #116ms
    ret = '' #6224ms
    for _ in range(int(input().rstrip())):
        num = int(input().rstrip())
        while cnt <= num:
            stack.append(cnt)
            #ret.append('+')
            ret += '+\n'
            cnt += 1

        if stack[-1] == num:
            stack.pop()
            #ret.append('-')
            ret += '-\n'
        else:
            break

    if stack:
        print("NO")
    else:
        #print('\n'.join(ret))
        print(ret.rstrip())

