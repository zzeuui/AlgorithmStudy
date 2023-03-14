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
