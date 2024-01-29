a, b = map(int, input().split())

prime = [True]*1000001
prime[0:2] = [False, False]
for i in range(2, int(1000001**0.5)):
    if prime[i]:
        prime[i+i::i] = [False]*len(prime[i+i::i])

for i in range(a, b+1):
    if prime[i]:
        print(i)
