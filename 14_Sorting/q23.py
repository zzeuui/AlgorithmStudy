"""
정답 1시간 (20분)

- 모든 조건마다 for문으로 데이터를 하나씩 정렬해서 시간초과됨
- 파이썬 내장함수 사용
: https://docs.python.org/ko/3/howto/sorting.html (정렬 안정성과 복잡한 정렬)
"""
import sys
input = sys.stdin.readline

def multisort(xs, specs):
    for key, reverse in reversed(specs):
        xs.sort(key=lambda xs: xs[key], reverse=reverse)
    return xs

def solution(n, students):
    # 1
    students = multisort(students,((1, True), (2, False), (3, True), (0, False)))
    return students

if __name__=='__main__':
    n = int(input())
    students = list()
    for _ in range(n):
        name, a, b, c = input().split()
        students.append((name, int(a), int(b), int(c)))

    for s in solution(n, students):
        print(s[0])
