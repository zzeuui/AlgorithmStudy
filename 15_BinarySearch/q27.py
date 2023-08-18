"""
정답 7분 (30분)

bisect 사용법 검색해서 품
**나중에 다시 풀어보기 
"""
from bisect import bisect_left, bisect_right

n, x = map(int, input().split())
nums = list(map(int, input().split()))

l = bisect_left(nums, x)
r = bisect_right(nums, x)

if r-l > 0:
    print(r-l)
else:
    print(-1)
