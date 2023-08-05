
def balanced_index(p):
    count = 0
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return i

def check_proper(p):
    cnt = 0
    for i in p:
        if i == '(':
            cnt += 1
        else:
            if cnt == 0:
                return False
            cnt -= 1

    return True

def solution(p):
    answer = ''
    if p == '':
        return answer

    #**최대한 단순하게 구현해, 실수 없이 동작
    index = balanced_index(p)
    u = p[:index+1]
    v = p[index+1:]

    if check_proper(u):
        answer = u + solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer = ')'
        u = list(u[1:-1]) #**첫 번째와 마지막 문자 제거
        #**뒤집기
        for i in range(len(u)):
            if u[i] == '(':
                u[i] == ')'
            else:
                u[i] == '('
        answer += "".join(u)
    return answer

