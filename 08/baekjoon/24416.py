def fib(n):
    global m1
    m1 += 1
    if n == 1 or n == 2:
        return 1
    else:
        return (fib(n-1)+fin(n-2))

def fibonacci(n):
    global m2
    f[0], f[1] = 1, 1
    for i in range(2, n):
        m2 += 1
        f[i] = f[i-1] + f[i-2]

    return f[n-1]

if __name__=='__main__':
    num = int(input())
    f = [1 for _ in range(num)]
    m1, m2 = 0, 0
    #print(fib(num), m1)
    print(fibonacci(num), m2)
