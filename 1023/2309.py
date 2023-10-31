from itertools import combinations

if __name__=='__main__':
    dwarf = [int(input()) for _ in range(9)]
    for com in list(combinations(dwarf, 7)):
        if sum(com) == 100:
            com = sorted(com)
            for c in com:
                print(c)

            break

