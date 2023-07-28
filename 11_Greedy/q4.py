#오답
"""
def func(m, i):
    for j in range(i+1, n):
        check_num.append(m+coins[j])
        func(m+coins[j], j)

n = int(input())
coins = list(map(int, input().split()))
coins.sort()

check_num = [c for c in coins]

func(coins[0], 0)
check_num = list(set(check_num))
check_num.sort()
for i, e in enumerate(check_num):
    if i+1 != e:
        print(i+1)
        break
"""

#매번 target인 금액도 만들 수 있는 지 확인
#현재 확인하는 동전 단위가 target 이하인지 확인
n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1
for x in data:
    
    if target < x:
        break
    
    target += x

print(target)
