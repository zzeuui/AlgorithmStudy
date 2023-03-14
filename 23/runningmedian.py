#bisect: 점프투파이썬 - https://wikidocs.net/105425
#bisect document: https://docs.python.org/ko/3/library/bisect.html

from sys import stdin
from bisect import insort_left

if __name__=='__main__':
    for _ in range(int(stdin.readline())):
        N, a, b = map(int, stdin.readline().split())
        ans = 0
        A = [1983]
        temp = 1983
        for i in range(N):
            ans += A[(len(A)-1)//2]
            temp = (temp * a + b) % 20090711
            insort_left(A, temp) #이진 분할 알고리즘으로 정렬된 리스트를 구성
        print(ans%20090711)

import heapq

def main():
    for _ in range(int(input().strip())):
        N, a, b = map(int, input().strip().split())
        cur = 1983
        nums = [cur]
        ans = 0
        
        max_heap = [-cur]
        heapq.heapify(max_heap)
        min_heap = [] 
        heapq.heapify(min_heap)
        for i in range(1, N):
            cur = (cur * a + b) % 20090711
            if(len(max_heap) > len(min_heap)):
                heapq.heappush(min_heap, cur)
            else:
                heapq.heappush(max_heap, -cur)
            if len(min_heap) > 0  and -max_heap[0] > min_heap[0]:
                t1 = -heapq.heappop(min_heap)
                t2 = -heapq.heappop(max_heap)
                heapq.heappush(min_heap, t2)
                heapq.heappush(max_heap, t1)
            ans += -max_heap[0]
                
        print((ans + 1983) % 20090711)
"""
if __name__ == '__main__':
    main()
"""
