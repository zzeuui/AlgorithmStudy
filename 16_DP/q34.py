"""
오답 1시간 33분
아무리 생각해도 답이 안나옴

책 풀이

가장 긴 증가하는 부분 수열(LIS, Longest Increasing Subsequence) 문제

d[i] = array[i]를 마지막 원소로 가지는 부분 수열의 최대 길이

모든 0<= j < i에 대해서,
d[i] = max(d[i], d[j]+1) if array[j] < array[i]
-> 현재 인덱스 i에 대해서, 그 앞의 모든 인덱스 j와 비교해 자기보다 작은 수가 있다면 +1을 해줌

*내림차순인 입력된 배열을 뒤집어 LIS 문제로 변환하여 풀이
"""

n = int(input())
array = list(map(int, input().split()))
array.reverse()

dp = [1]*n

for i in range(1, n):
    for j in range(0, i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(n-max(dp))

"""
- https://one10004.tistory.com/217
위 방법은 두개의 for문을 사용해 O(N^2)의 시간 안에 풀이됨
이분 탐색을 사용해 O(NlogN)으로 풀이할 수 있음
"""

from bisect import bisect_left

array = [5, 2, 1, 4, 3, 5]
dp = [1]
x = [array[0]]

for i in range(1, len(array)):
    if array[i] > x[-1]:
        x.append(array[i])
        dp.append(dp[-1]+1)

    else:
        idx = bisect_left(x, array[i])
        x[idx] = array[i]

