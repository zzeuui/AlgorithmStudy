n = int(input())

if n == 0:
    print(0)
else:
    ret = 1
    for i in range(2, n+1):
        ret *= i

    cnt = 0
    for e in list(str(ret))[::-1]:
        if e != '0':
            break
        else:
            cnt += 1

    print(cnt)
