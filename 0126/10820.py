import sys
input = sys.stdin.readline

if __name__=='__main__':
    while True:
        seq = input()[:-1]
        if not seq: break

        cnt = [0]*4

        for s in seq:
            if 'a' <= s <= 'z':
                cnt[0] += 1
            elif 'A' <= s <= 'Z':
                cnt[1] += 1
            elif '0' <= s <= '9':
                cnt[2] += 1
            elif s == ' ':
                cnt[3] += 1

        print(*cnt)
