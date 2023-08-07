"""
정답 30분 (20분)

합계 100.0

fail[i]나 num이 0일 때를 처리하는 걸 생각하지 못해서 시간이 좀 걸림 
"""
def solution(N, stages):
    stages.sort()
    fail = [0]*(N+2)
    num = len(stages)

    while stages:
        i = stages.pop()
        fail[i] += 1

    fail = fail[1:-1]
    for i in range(0, N):
        if fail[i] == 0 or num == 0:
            fail[i] = (i+1, 0)
        else:
            fail[i], num_peo = (i+1, fail[i]/num), num-fail[i]

    fail = sorted(fail, key=lambda x:x[1], reverse=True)
    answer = [i for i, r in fail]

    return answer
