"""
오답 

binary search 구현 다 까먹었네..
재귀호출로,
- 현재 값보다 타켓이 작으면 왼쪽
- 현재 값보다 타켓이 크면 오른쪽
- 현재 값이 타겟이면 리턴
- start가 end보다 커지면 타켓이 없음
"""
def binary_search(nums, start, end):
    if start > end:
        return None
    mid = (start+end) // 2

    if nums[mid] == mid:
        return mid
    elif nums[mid] > mid:
        return binary_search(nums, start, mid-1)
    else:
        return binary_search(nums, mid+1, end)

n = int(input())
nums = list(map(int, input().split()))

index = binary_search(nums, 0, n-1)

if index == None:
    print(-1)
else:
    print(index)
