import sys
input = sys.stdin.readline

def gcd(n, m):
    while m != 0:
        r = n%m
        n, m = m, r

    return n

if __name__=='__main__':
    for _ in range(int(input())):
        nums = list(map(int, input().rstrip().split()))[1:]

        ret = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                ret += gcd(nums[i], nums[j])

        print(ret)
