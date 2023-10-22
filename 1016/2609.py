import sys
input = sys.stdin.readline

m, n = map(int, input().rstrip().split())
v1 = max(m, n)
v2 = min(m, n)

i = 1
while True:
    if (v1*i) % v2 == 0:
        r1 = v1*i
        break
    i += 1

i = v2
while True:
    if (v1%i==0) and (v2%i==0):
        r2 = i
        break
    i -= 1

print(r2)
print(r1)
