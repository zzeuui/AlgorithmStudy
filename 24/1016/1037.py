import sys
input = sys.stdin.readline

if __name__=='__main__':
    num = int(input())
    nums = list(map(int, input().rstrip().split()))
    nums.sort()

    if len(nums) == 1:
        print(nums[0]**2)
    else:
        print(nums[0]*nums[-1])
