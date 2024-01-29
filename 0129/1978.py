n = int(input())
nums = list(map(int, input().split()))

prime = [True]*1001
prime[0:2] = [False, False]
for i in range(2, 1001):
    if prime[i]:
        prime[i+i::i] = [False]*len(prime[i+i::i])

cnt = 0
for i in nums:
    if prime[i]:
        cnt += 1

print(cnt)
