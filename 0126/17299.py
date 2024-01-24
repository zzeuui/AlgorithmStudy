import sys
input = sys.stdin.readline

from collections import Counter

if __name__=='__main__':
    n = int(input())
    nums = list(map(int, input().split()))
    F = Counter(nums)
    NGF = [-1]*n
    stack = [0]

    for i in range(1, n):
        while stack and F[nums[stack[-1]]] < F[nums[i]]:
            NGF[stack.pop()] = nums[i]

        stack.append(i)

    print(*NGF)
