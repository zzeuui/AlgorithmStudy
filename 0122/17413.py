import sys
input = sys.stdin.readline

if __name__=='__main__':
    sen = list(input().rstrip())

    ret = list()

    temp = list()
    while sen:
        s = sen.pop(0)
        if s == '<':
            ret.append(''.join(temp)[::-1])
            temp = list()
            temp.append(s)
            while s != '>':
                s = sen.pop(0)
                temp.append(s)
            ret.append(''.join(temp))
            temp = list()
        else:
            temp.append(s)

        if s == ' ':
            ret.append(''.join(temp)[::-1])
            temp = list()

    ret.append(''.join(temp)[::-1])

    ret = [r.lstrip() +' ' if ' ' in r and '<' not in r else r for r in ret]
    print(''.join(ret).strip())
