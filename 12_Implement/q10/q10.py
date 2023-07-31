"""
오답
정확성: 30.0
합계: 30.0 / 100.0
"""

import copy

def check_kl(key, lock):
    key = [e for ele in key for e in ele]
    lock = [e for ele in lock for e in ele]
    
    for k, l in zip(key, lock):
        if k+l != 1:
            return False
        
    return True
    
def move_key(key, mode):
    """
    mode:
        0(int): right
        M(int): left
        U(str): up
        D(str): down
    """
    ret = list()
    M = len(key[0])
    if mode == 'U':
        ret = key[1:]
        ret.insert(M, [0]*M)
    elif mode == 'D':
        ret = key[:-1]
        ret.insert(0, [0]*M)
    else:
        for ele in key:
            ele.insert(mode, 0)
            if mode == 0:
                ret.append(ele[:-1])
            else:
                ret.append(ele[1:])
        
    return ret

def rotate_key(key):
    """
    rotate right
    """
    M = len(key[0])
    ret = list()
    for col in range(M):
        temp = list()
        for row in range(M):
            temp.insert(0, key[row][col])
            
        ret.append(temp)
        
    return ret

def one_action(key, lock, mode):
    if mode == 'R':
        key = rotate_key(key)
    else:
        key = move_key(key, mode)
    
    return key, check_kl(key, lock)

def one_iter(key, lock, mode, M):
    for _ in range(M-1):
        key, answer = one_action(key, lock, mode)
        yield key, answer

def each_case(key, lock, mode, M):
    answer = False
    for key, answer in one_iter(key, lock, mode, M):
        if answer: return answer
        for m in ['U', 'D']:
            for _, answer in one_iter(key, lock, m, M):
                if answer: return answer
            
    return answer

def solution(key, lock):
    M = len(key[0])
    answer = False
    
    #90도씩 시계방향으로 4번 회전
    for _ in range(4):
        key, answer = one_action(key, lock, 'R')
        if answer: return answer
        
        for m in ['U', 'D']:           
            for _, answer in one_iter(key, lock, m, M):
                if answer: return answer
        
        ori_key = copy.deepcopy(key)
        for m in [0, M]:
            key = copy.deepcopy(ori_key)
            answer = each_case(key, lock, m, M)
            if answer: return answer
        
    return answer 
