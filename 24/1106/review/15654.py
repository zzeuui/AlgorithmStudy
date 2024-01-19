
n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

s = list()
def permt():
    if len(s) == m:
        print(' '.join(map(str, s)))

    for i in nums:
        if i not in s:
            s.append(i)
            permt()
            s.pop()

permt()

#from itertools import permutations
#print(list(permutations(nums, m)))
