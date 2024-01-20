import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
arr = [i for i in range(1, n+1)]
answer = list()
ind = 0

for _ in range(n):
    ind += k-1
    if ind >= len(arr):
        ind = ind%len(arr)

    answer.append(arr.pop(ind))

print(str(answer).replace('[','<').replace(']','>'))
