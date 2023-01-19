if __name__=='__main__':
    n = int(input())
    i = '666'
    m = 1
    if n == 1:
        print(i)
    else:
        while True:
            i = str(int(i)+1)
            if '666' in i:
                m += 1

            if m == n:
                break
        print(i)
