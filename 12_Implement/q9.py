#못 품
def solution(s):
    answer = len(s)
    #1개씩 최대 그룹으로 나뉘었을 때부터 최소 두 그룹으로 나뉘었을 때까지
    for step in range(1, len(s)//2+1):
        compressed = ""
        prev = s[0:step] 
        cnt = 1

        #단위(step) 크기만큼 증가시킴
        for j in range(step, len(s), step):
            if prev == s[j:j+step]:
                cnt += 1
            else:
                compressed += str(cnt) + prev if cnt >= 2 else prev
                prev = s[j:j+step]
                cnt = 1

        compressed += str(cnt) + prev if cnt >= 2 else prev
        answer = min(answer, len(compressed))
    
    return answer

s = input()
print(solution(s))
