# 8분
num = list(map(int, list(input())))
div = int(len(num)/2)

if sum(num[:div]) == sum(num[div:]):
    print('LUCKY')
else:
    print('READY')
