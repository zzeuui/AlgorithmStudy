
def flip(tree):

    tree.reverse()
    temp = list(tree[0])
    temp.extend(tree[3:5])
    temp.extend(tree[1:3])

    return temp

if __name__=='__main__':
    case_n = input()

    for _ in range(int(case_n)):
        tree = list(input())

        es = list()

        while tree:
            e = tree.pop()

            es.append(e)

            if e == 'x' and len(tree) > 0:
                temp = es[-5:]
                del es[-5:]

                temp = flip(temp)
                temp = ''.join(temp)
                es.append(temp)

        es = flip(es)
        print(''.join(es))
