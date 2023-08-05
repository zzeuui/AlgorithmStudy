"""
오답 (50분)

정확성 32.0
합계 32.0 / 100.0
"""
#2
def seond(ps):
    if len(ps) == 0:
        return ps, ps
    
    l, r = 0, 0
    u = list()
    for i, p in enumerate(ps):
        if p == '(':
            u.append(p)
            l += 1
        elif p == ')':
            u.append(p)
            r += 1
        if l == r:
            break
    v = ps[i+1:]
    
    return u, v

def check_u(u):
    if len(u) == 0:
        return True
    elif u[0] == ')':
        return False
    
    temp = [u[0]]
    for s in u[1:]:
        if s == '(':
            temp.append(s)
        else:
            temp.pop(-1)
    
    if len(temp) == 0:
        return True
    else:
        return False

#3-4
def third_four(ps, answer):
    if len(ps) == 0:
        return ''
    
    #2
    u, v = seond(ps)
    print(u, v)
    #3
    if check_u(u):
        answer = third_four(v, answer)
        answer = ''.join(u) + answer
        return answer
    #4
    else:
        answer = '('+answer
        answer += third_four(v, answer)
        answer = answer+')'
    
    u.pop(0)
    u.pop(-1)
    temp = ''
    for s in u:
        if s == ")":
            temp += "("
        else:
            temp += ")"
    
    return answer + temp
        
def solution(p):
    ps = list(p)
    if len(ps) == 0:
        return ''
    
    answer = ''
    answer = third_four(ps, answer)
    
    return answer
