if __name__=='__main__':
    s = list(map(int, list(input())))

    num = {0:0, 1:0}

    for i in range(1, len(s)):
        if s[i-1] != s[i]:
            num[s[i-1]] += 1

        if i == len(s)-1:
            num[s[i]] += 1

    print(min(num[0], num[1]))
