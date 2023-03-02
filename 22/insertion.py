# c++: https://damper.tistory.com/37

import sys
input = sys.stdin.readline

if __name__=='__main__':

    for _ in range(int(input())):
        N = int(input())
        A = tuple(map(int, input().split()))
        B = [ n for n in range(1, N+1)]
        C = [0] * N

        for i in range(N-1, -1, -1):
            t = B[i-A[i]] #남은 숫자들중 A[i]만큼 큰 수를 가진 값
            C[i] = t 
            B.pop(i-A[i]) #제외

        for i in range(N):
            print(C[i], end=" ")

        print("")
