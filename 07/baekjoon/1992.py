def crop_paper(paper, length):
    length_h = int(length/2)

    ids = [0, 1, length, length+1]
    cnt = 0

    ret = list()
    while True:
        if cnt < length_h:
            quad = [paper[ids[0]], paper[ids[1]], paper[ids[2]], paper[ids[3]]]
            try: f = sum(quad)
            except: f = -1

            if f == 4: ret.append(1)
            elif f == 0: ret.append(0)
            else: ret.append(quad)

        elif cnt == length-1:
            cnt = -1

        ids = [i+2 for i in ids]
        cnt += 1
        if ids[-1] > length*length: break

    if length > 2:
        length = int(length/2)
        ret = crop_paper(ret, length)
    else:
        return ret

    return ret

if __name__=='__main__':
    length = int(input())
    length_h = int(length/2)

    paper = list()
    for _ in range(length):
        paper.extend(list(map(int, list(input()))))

    ret = crop_paper(paper, length)
    ret = str(ret).replace('[', '(').replace(']', ')').replace(' ', '').replace(',', '')
    ret = (ret[1:])[:-1]
    print(ret)
