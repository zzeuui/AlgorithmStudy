"""
정답 28분 (30분)

처음에 list랑 sort()로 구현했다가 시간 초과
원소 중 가장 작은 두 수를 더해가야하기 때문에 heapq로 구현
"""

import heapq
import sys
input = sys.stdin.readline

def solution(N, cards):
    ret = 0
    while len(cards) > 1:
        a = heapq.heappop(cards)
        b = heapq.heappop(cards)
        c = a+b
        heapq.heappush(cards, c)
        ret += c

    return ret

if __name__=='__main__':
    N = int(input())
    cards = list()
    for _ in range(N):
        heapq.heappush(cards, int(input()))

    print(solution(N, cards))
