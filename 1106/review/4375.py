while True:
    try:
        n = int(input())
    except:
        break

    divisor = 1

    while True:
        if divisor % n == 0:
            break

        divisor = (divisor*10)+1

    print(len(str(divisor)))
