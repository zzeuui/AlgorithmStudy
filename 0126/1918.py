seq = list(input())
stack = list()
ans = ''

for s in seq:

    #문자열은 바로 추가
    #문자열의 연산 순서는 바뀌지 않음
    if s.isalpha():
        ans += s

    # '(' 이면 stack에 일단 추가
    elif s == '(':
        stack.append(s)

    # 우선 순위가 높은 연산일 경우
    elif s in ['*', '/']:
        #앞선 연산이 '*'이나 '/'일 때 pop
        while stack and (stack[-1] in ['*', '/']):
            ans += stack.pop()

        # 현재 '*'나 '/'는 stack에 넣기
        stack.append(s)

    elif s in ['+', '-']:
        # '('을 제외하고 이전에 쌓인 연산들을 모두 pop
        while stack and stack[-1] != '(':
            ans += stack.pop()

        stack.append(s)

    else:
        # ')' 이라면 '('까지 다 정답으로 추가함
        while stack and stack[-1] != '(':
            ans += stack.pop()

        stack.pop() #'(' 제거

while stack: #남아 있는 문자 정답으로 추가하기
    ans += stack.pop()

print(ans)
