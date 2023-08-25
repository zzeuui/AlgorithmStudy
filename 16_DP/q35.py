"""
오답 시간 초과
if __name__=='__main__':
    n = int(input())
    nums = [1, 2, 3, 4, 5]

    i = 6
    while len(nums) < n:
        for e in nums[::-1][1:]:
            if i%e == 0 and e != 1 and int(i/e) in nums:
                nums.append(i)
                break
        i += 1
"""

"""
못생긴 수에 2, 3 혹은 5를 곱한 수 또한 '못생긴 수'에 해당
가장 작은 못생긴 수부터 오름차순으로, 각 배수를 곱한 값도 못생긴 수가 될 수 있도록 처리
"""
n = int(input())

ugly = [0]*n
ugly = 1

#2배, 3배, 5배를 위한 인덱스
i2 = i3 = i5 = 0
#처음에 곱셈값을 초기화
next2, next3, next5 = 2, 3, 5

for l in range(1, n):
    #가능한 곱셈 결과 중 *가장 작은 수*를 선택
    #현재 *가장 앞*의 인덱스에 적용
    ugly[l] = min(next2, next3, next5)

    if ugly[l] == next2:
        i2 += 1 #앞의 못생긴 수들에 대해 하나씩 2곱함
        next2 = ugly[i2]*2
    if ugly[l] == next3:
        i3 += 1 #앞의 못생긴 수들에 대해 하나씩 3을 곱함
        next3 = ugly[i3]*3
    if ugly[l] == next5:
        i5 += 1 #앞의 못생긴 수들에 대해 하나씩 5를 곱함
        next5 = ugly[i5]*5

    print(ugly[n-1])
