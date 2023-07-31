# 8분
line = list(input())
line.sort()

ind = None
for i, s in enumerate(line):
    if ord(s) >= ord('A'):
        ind = i
        break

if ind is not None:
    num = sum(list(map(int, line[:ind])))
    alp = ''.join(line[ind:])
    print(alp+str(num))

"""
파이썬 내장 함수
- isalpha(): 알파벳인지 확인
- isdigit(): 숫자인지 확인
- isalnum(): 알파벳이나 숫자인지 확인

*공백이나 다른 특수문자가 포함되면 False 반환
"""
