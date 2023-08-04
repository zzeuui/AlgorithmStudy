"""
전체 친구 수는 8이기 때문에, 친구를 나열하는 모든 경우의 수를 각각 확인
문제 풀이를 간단히 하기 위해 길이를 2배로 늘려 '원형'을 일자형태로 만드는 작업을 하면 유리함

Example)
취약지점 1, 3, 4, 9, 10(5곳) -> 원형 1, 3, 4, 9, 10, 13, 15, 16, 21, 22
3명의 친구 3m, 5m, 7m
9부터 16까지 7m 친구가 5곳을 모두 방문할 수 있음
"""

from itertools import permutations

def solution(n, weak, dist):
    length = len(weak)
    for i in range(length):
        weak.append(weak[i]+n)
    answer = len(dist)+1

    for start in range(length):
        for friends in list(permutations(dist, len(dist))):
            cnt = 1
            # 해당 친구가 점검할 수 있는 마지막 위치
            position = weak[start] + friends[cnt - 1]
            # 시작점부터 모든 취약 지점을 확인
            for index in range(start, start+length):
                # 점검할 수 있는 위치를 벗어나는 경우
                if position < weak[index]:
                    cnt += 1 # 새로운 친구를 투입
                    if cnt > len(dist): # 더 투입할 수 없으면 종료
                        break
                    position = weak[start] + friends[cnt - 1]
            answer = min(answer, cnt)

    if answer > len(dist):
        return -1
    else:
        return answer

