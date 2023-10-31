n, m = map(int, input().split())

v1 = min(n, m)
v2 = max(n, m)
r1, r2 = v1, v2

while True:
    if v2 % r1 == 0 and v1 % r1 == 0:
        break
    else:
        r1 -= 1
print(r1)

i = 1
while True:
    if r2 % v1 == 0:
        break
    else:
        i += 1
        r2 = (v2*i)
print(r2)
