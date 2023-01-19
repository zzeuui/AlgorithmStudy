def crop_paper(paper, leng):
    leng_h = int(leng/3) #1

    ids = [0, 1, 2, leng, leng+1, leng+2, leng*2, leng*2+1, leng*2+2]
    cnt = 0

    ret = list()
    while True:
        if cnt < leng_h:
            quad = list()
            for i in ids:
                quad.append(paper[i])

            try: f = sum(quad)
            except: f = -1

            if f == 9: ret.append(1)
            elif f == 0 and len(list(set(quad)))==1: ret.append(0)
            elif f == -9: ret.append(-1)
            else: ret.append(quad)

        elif cnt == leng-1:
            cnt = -1

        ids = [i+3 for i in ids]
        cnt += 1
        if ids[-1] > leng*leng: break

    if leng > 3:
        leng = int(leng/3)
        ret = crop_paper(ret, leng)
    else:
        return ret

    return ret

def unzip_tree(ret, num):
    while ret:
        ele = ret.pop()

        try:
            l = len(ele)
        except:
            l = -1

        if  l == -1:
            num[ele+1] += 1
        else:
            num = unzip_tree(ele, num)

    return num

if __name__=='__main__':
    length = int(input())

    paper = list()
    for _ in range(length):
        paper.extend(list(map(int, input().split(' '))))

    num = [0, 0, 0]
    if len(paper) == 1:
        num[paper[0]+1] = 1

    ret = crop_paper(paper, length)
    num = unzip_tree(ret, num)

    for n in num:
        print(n)
