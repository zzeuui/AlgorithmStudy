
n, m = map(int, input().split())
nums = [i for i in range(1, n+1)]

s = list()
def permt():
    if len(s) == m:
        print(' '.join(map(str, s)))

    for i in range(1, n+1):
        if i not in s:
            s.append(i)
            permt()
            s.pop()

permt()

#from itertools import permutations
#print(list(permutations(nums, m)))
