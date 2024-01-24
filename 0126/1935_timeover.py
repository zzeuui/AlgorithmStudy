import sys
input = sys.stdin.readline

if __name__=='__main__':
    n = int(input())
    seq = list(input().rstrip())
    al_di = {chr(65+i): int(input()) for i in range(n)}
    seq = [al_di[s] if s in al_di.keys() else s for s in seq]
    
    seq_temp = list()
    non_op = 0
    ret = 0
    
    while seq:
        s = seq.pop()
        seq_temp.append(s)

        if s not in ['+', '-', '/', '*']:
            non_op += 1
            if non_op == 2:
                a = seq_temp.pop()
                b = seq_temp.pop()
                op = seq_temp.pop()

                ret = eval(f'{a}{op}{b}')
                seq_temp.append(ret)
                non_op = 0
        else:
            non_op = 0

        if not seq:
            if len(seq_temp) == 1:
                break
            seq, seq_temp = seq_temp[::-1], seq
            non_op = 0

    print(f'{seq_temp[0]:.2f}')
