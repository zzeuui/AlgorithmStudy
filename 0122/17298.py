import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().rstrip().split()))
ret = [-1]*n
stack = [0]

for i in range(1, n):
    while stack and A[stack[-1]] < A[i]:
        ret[stack.pop()] = A[i]

    stack.append(i)

print(*ret)
