def possible(answer):
    for x, y, stuff in answer:
        if stuff == 0:
            if y == 0 or [x-1,y,1] in answer or [x,y,1] in answer or [x,y-1,0]:
                # y == 0: 바닥
                # [x-1,y,1] or [x,y,1] : 보의 한쪽 끝부분 위
                # [x,y-1,0] : 다른 기둥 위
                continue
            return False
        elif stuff == 1:
            if [x,y-1,0] in answer or [x+1,y-1, 0] in answer or ([x-1,y,1] in answer and [x+1,y,1] in answer):
                #[x,y-1,0] or [x+1,y-1,0]: 기둥 위
                #([x-1,y,1] and [x+1,y,1]): 양쪽 보에 연결
                continue
            return False

    return True

def solution(n, build_frame):
    answer=[]
    for frame in build_frame:
        x,y,stuff,operate = frame
        if operate == 0:
            #일단 삭제해보고 가능한 구조물인지 확인
            answer.remove([x,y,stuff]) 
            if not possible(answer):
                answer.append([x,y,stuff])

        if operate == 1:
            #일단 설치해보고 가능한 구조물인지 확인
            answer.append([x,y,stuff])
            if not possible(answer):
                answer.remove([x,y,stuff])

    return sorted(answer)


