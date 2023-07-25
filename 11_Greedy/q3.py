# 11분
string = list(map(int, list(input())))

pre_s = string.pop(0)

cnt_zero = 0
cnt_one = 0

while string:
    cur_s = string.pop(0)
    if pre_s != cur_s:
        if pre_s == 0:
            cnt_zero += 1
        else:
            cnt_one += 1
        pre_s = cur_s

if cur_s:
    cnt_one += 1
else:
    cnt_zero += 1

print(min(cnt_one, cnt_zero))
