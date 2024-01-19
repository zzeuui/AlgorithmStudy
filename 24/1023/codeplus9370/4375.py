while True:
    try:
        n = int(input())
    except:
        break

    x = 1
    while True:
        if x % n == 0:
            break
        else:
            x = (x*10)+1
    print(len(list(str(x))))
