if __name__=='__main__':
    n = list(map(int, list(input())))
    
    idx = len(n)//2
    if sum(n[:idx]) == sum(n[idx:]):
        print('LUCKY')
    else:
        print('READY')
