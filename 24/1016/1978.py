import sys
input =sys.stdin.readline

n = int(input())
nums = list(map(int, input().rstrip().split()))

ret = 0
for num in nums:
    if num > 1:
        ret += 1
        for i in range(2, num):
            if num % i == 0:
                ret -= 1
                break
print(ret)
