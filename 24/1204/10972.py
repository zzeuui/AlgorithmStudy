"""
뒤에서부터 뒷 값이 앞 값보다 큰 경우를 찾는다
: 앞 값 뒤에 존재하는 숫자들로 구성된 가능한 모든 오름차순 순열이 끝난 시점

뒤에서부터 비교하며, 앞 값보다 큰 값이 있다면 교환한다
: 그렇다면, 뒤에 존재하는 숫자들 중 앞 값보다 하나 더 큰 값이랑 앞 값이랑 교환해야,
앞 값의 다음 오른차순 순열을 만들 수 있음.

뒷 값에 해당하는 인덱스부터 끝까지 오름차순 정렬한다.
: 앞 값은 하나 더 큰 수로 바뀌었고, 이제 다시 앞 값 뒤에 존재하는 숫자들로 구성된 오름차순 순열이되어야함


오름차순 정렬임으로 다음 순열은 큰 값 하나를 앞으로 옮긴 순열.
큰 값 하나를 앞으로 옮긴, 그 뒤는 오름차순 정렬이 되어야함.
"""
import sys
input = sys.stdin.readline

def create_next(permt):
    global n 

    for i in range(n-1, 0, -1):
        if permt[i] > permt[i-1]:
            for j in range(n-1, 0, -1):
                if permt[i-1] < permt[j]:
                    permt[i-1], permt[j] = permt[j], permt[i-1]
                    break
            permt[i:] = sorted(permt[i:])
            return permt

    return False

if __name__=='__main__':
    n = int(input())
    permt = list(map(int, input().rstrip().split()))

    if not create_next(permt):
        print(-1)
    else:
        print(' '.join(list(map(str, permt))))
