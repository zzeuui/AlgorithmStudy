import sys
input = sys.stdin.readline

if __name__=='__main__':
    for _ in range(int(input())):
        a, b = map(int, input().split())
        ret = a*b

	# r이 a%b의 나머지라고 했을때
        # a와 b의 최대공약수는 b와 r의 최대공약수와 동일하고
        # r이 0일때 b가 최대공약수가 됨
        while b != 0:
            r = a%b
            a, b = b, r

        #최소공배수는 두 수의 곱을 최대공약수로 나눠 구할 수 있음
        print(int(ret/a))
