import sys
input = sys.stdin.readline

if __name__=='__main__':
    cnt = {chr(i):0 for i in range(ord('a'), ord('z')+1)}

    seq = input().rstrip()

    for s in seq:
        cnt[s] += 1

    ret = [v for k, v in cnt.items()]

    print(*ret)
