import sys
input = sys.stdin.readline

if __name__=='__main__':
    
    while True:
        try:
            n = int(input())
        except:
            break

        i = 1
        m = 1
        while True:
            if i % n == 0:
                print(m)
                break
            i = i*10+1
            m += 1
