n = int(input())
peo = list(map(int, input().split()))

"""
#오답 큰 수부터 처리함 (14분)
peo.sort()

ret = 0
temp = 0

while peo:
    p = peo.pop()
    if not temp:
        temp = p-1
        ret += 1
    else:
        temp -= 1

if temp > 0:
    ret -= 1

print(ret)
"""

peo.sort()
ret = 0
cnt = 0

for p in peo:
    cnt += 1
    if cnt == p:
        ret += 1
        cnt = 0

print(ret)
