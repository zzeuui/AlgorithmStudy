import sys
input = sys.stdin.readline

if __name__=='__main__':
    bi = list(map(int, list(input().rstrip())))[::-1]

    ret = list()
    for i in range(len(bi)//3):
        ret.append(bi[i*3] + bi[i*3+1]*2 + bi[i*3+2]*4)

    if len(bi) % 3 > 0:
        remi = bi[(len(bi)//3)*3:]
        remi_oc = 0
        for i, r in enumerate(remi):
            remi_oc += r*(2**i)

        ret.append(remi_oc)

    print(''.join(list(map(str, ret[::-1]))))

