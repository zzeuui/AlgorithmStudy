import bisect
import statistics as st
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def binary_search(rooms, start, end, C):
    if C <= 0 or start > end: #or index range error
        return 1e9

    mean = st.mean(rooms)
    mid = 0
    pre = abs(mean - rooms[mid])
    for m, r2 in enumerate(rooms):
        if pre > abs(mean-r2):
            mid = m
            pre = abs(mean-r2)

    C -= 1

    min1 = min(rooms[mid]-rooms[start], rooms[end] - rooms[mid])
    if rooms[mid] > min1:
        min2 = min(min1, binary_search(rooms, mid, end, C))
    else:
        min2 = min(min1, binary_search(rooms, start, mid, C))

    return max(min1, min2)


def solution(N, C, rooms):
    if C == 2:
        return rooms[-1] - rooms[0]

    C -= 2

    return binary_search(rooms, 0, N-1, C)
    
if __name__=='__main__':
    N, C = map(int, input().split())
    rooms = list()
    for _ in range(N):
        bisect.insort(rooms, int(input()))

    print(solution(N, C, rooms))
