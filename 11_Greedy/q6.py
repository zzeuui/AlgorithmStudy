"""
오답

정확성: 12.1
효율성: 7.1
합계: 19.2 / 100.0

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    v = k // len(food_times)
    d = k % len(food_times)
    food_times = [f-v for f in food_times]
    minus = [f for f in food_times if f < 0]
    d += sum(minus)*-1

    i = 0
    while d > 0:
        if food_times[i] - 1 >= 0:
            food_times[i] -= 1
            d -= 1
            if food_times[i] > 0:
                return i+1

        i += 1

    if sum(food_times) == 0:
        return -1

    for j in range(i, len(food_times)):
        if food_times[j] > 0:
            return j+1
"""

"""
우선순위 큐를 활용해 시간이 적게 걸리는 음식부터 제거해 나가는 방식으로 구현
남은 시간 -= 남은 음식 수 * 현재 가장 적게 걸리는 음식의 시간
남은 시간이 음수가 되면, 남은 음식들을 나열한 뒤 계산
"""

import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1))

    sum_value = 0
    previous = 0
    length = len(food_times)

    #sum_value + (현재의 음식 시간 - 이전 음식 시간) * 현재 음식 개수와 k 비교
    while sum_value+ ((q[0][0] - previous)*length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now-previous)*length
        lenght -= 1
        previous = now

    result = sorted(q, k=lambda x:x[1])
    return result[(k-sum_value)%length][1]
