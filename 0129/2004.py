n, m = map(int, input().split())

#0의 개수 == *10의 개수 == *(2*5)의 개수
# 2가 곱해지는 횟수와 5가 곱해지는 횟수를 비교해 적은 수를 선택
# 즉, 소인수분해를 수행했을 때 2의 지수와 5의 지수를 파악함
def cnt(n, k):
    cnt = 0
    while n != 0:
        n = n // k
        cnt += n
    return cnt

# 조합의 수 nCr은 n!/r!(n-r)!이고, 지수는 계산할 수 있음
# 2^2 * 2^1 = 2^3
# 2^2 / 2^1 = 2^1
two = cnt(n, 2) - (cnt(n-m, 2) + cnt(m, 2))
five = cnt(n, 5) - (cnt(n-m, 5) + cnt(m, 5))
print(min(two, five))
