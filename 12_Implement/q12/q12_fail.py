"""
기둥과 보가 설치될 수 있는 위치를 체크하면서 설치하려고 해봤고,
삭제는 어떻게 해야할 지 모르겠음.
** 구조물이 정상 상태인걸 어떻게 구현하지
"""
def solution(n, build_frame):
    answer = []
    
    valid_colu = [[0]*(n+1) for _ in range(n+1)]
    valid_beam = [[0]*(n+1) for _ in range(n+1)]

    for i in range(n+1):
        valid_colu[i][0] = 1

    for action in build_frame:
        x, y, a, b = action
        if b:
            if a:
                if valid_beam[x][y] == 1 or (valid_colu[x][y] == 1 and valid_colu[x+1][y] == 1):
                    answer.append([x, y, a])
                    valid_colu[x+1][y] = 1

            else:
                if valid_colu[x][y] == 1:
                    answer.append([x, y, a])
                    valid_colu[x][y+1] = 1
                    valid_beam[x][y+1] = 1
                    if x-1 >= 0:
                        valid_beam[x-1][y+1] = 1

        else:
            if a:
            else:

    answer.sort()

    return answer
