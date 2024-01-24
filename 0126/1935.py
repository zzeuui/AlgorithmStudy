import sys
input = sys.stdin.readline

n = int(input())
word = input().rstrip()
num = [int(input()) for _ in range(n)]

stack = list()

for i in word:
    if 'A' <= i <= 'Z':
        stack.append(num[ord(i)-ord('A')])

    else:
        n2 = stack.pop()
        n1 = stack.pop()

        ret = eval(f'{n1}{i}{n2}')
        stack.append(ret)

print(f'{stack[0]:.2f}')
