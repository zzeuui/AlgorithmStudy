import sys
input = sys.stdin.readline

def f(seq):
    ret = list()
    while seq:
        s = seq.pop(0)

        if 'A' <= s <= 'Z':
            ret.append(s)

        else:
            nt = seq.pop(0)
            
            if ret[-1] in ['+', '-'] and s in ['*', '/']:
                o = ret.pop()
                ret.append(nt)
                ret.append(s)
                ret.append(o)
            else:
                ret.append(nt)
                ret.append(s)

    print(ret)
    return ret

if __name__=='__main__':
    seq = list(input().rstrip())
    
    ret = f(seq)
    
    print(ret)
    print(''.join(ret))
