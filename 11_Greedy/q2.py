# 6분
nums = list(map(int, list(input())))
ret = max(nums[0]+nums[1], nums[0]*nums[1])

for n in nums[2:]:
    ret = max(ret+n, ret*n)

print(ret)
    
    
