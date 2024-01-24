import sys
input = sys.stdin.readline

if __name__=='__main__':
    cnt = {chr(i):-1 for i in range(ord('a'), ord('z')+1)}

    seq = input().rstrip()

    for i, s in enumerate(seq):
        if cnt[s] == -1:
            cnt[s] = i

    ret = [v for k, v in cnt.items()]

    print(*ret)
