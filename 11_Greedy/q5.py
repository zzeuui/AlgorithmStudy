n, m = map(int, input().split())
data = list(map(int, input().split()))

#오답(9분)
"""
cnt = 0
for i in range(n):
    for j in range(i+1, n):
        if data[i] != data[j]:
            cnt += 1

print(cnt)
"""

"""
각 무게 별 볼링공의 개수를 확인한 후
A가 특정 무게의 볼링공을 선택했을 때, B가 볼링공을 선택할 수 있는 경우의 수를 계산
A가 볼링공을 선택한 경우의 수 * 나머지 볼링공에서 B가 선택할 수 있는 경우의 수

무게 1 볼링공: 1개
무게 2 볼링공: 2개
무게 3 볼링공: 3개

A가 무게 1 선택 => 1*4(무게2 + 무게 3) = 4
A가 무게 2 선택 => 2*2(무게 3) = 4
A가 무게 3 선택 => 2*0(이미 다 조합함) = 0

답: 4+4+0 = 8
"""

array = [0]*11

for x in data:
    array[x] += 1

ret = 0

for i in range(1, m+1):
    n -= array[i]
    ret += array[i]*n

print(ret)
