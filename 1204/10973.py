"""
뒤에서부터 뒷 값이 앞 값보다 작은 경우를 찾는다
뒤에서부터 비교하며, 앞 값보다 작은 값이 있다면 교환한다.
뒷값에 해당하는 인덱스부터 끝까지 내림차순 정렬한다.


#오름차순 정렬임으로 다음 순열은 큰 값 하나를 앞으로 옮긴 순열.
#큰 값 하나를 앞으로 옮긴, 그 뒤는 오름차순 정렬이 되어야함.
"""
import sys
input = sys.stdin.readline

def create_next(permt):
    global n 

    for i in range(n-1, 0, -1):
        if permt[i] < permt[i-1]:
            for j in range(n-1, 0, -1):
                if permt[i-1] > permt[j]:
                    permt[i-1], permt[j] = permt[j], permt[i-1]
                    break
            permt[i:] = sorted(permt[i:], reverse=True)
            return permt

    return False

if __name__=='__main__':
    n = int(input())
    permt = list(map(int, input().rstrip().split()))

    if not create_next(permt):
        print(-1)
    else:
        print(' '.join(list(map(str, permt))))
