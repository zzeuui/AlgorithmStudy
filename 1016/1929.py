"""
 어떤 수 n이 1과 자신이 아닌 두 수의 곱으로 이뤄짐(소수가 아님)
  ==> n = a*b, n' = n**0.5
  
  만약 a >= n' 이면, a*b = n = n'*n'이므로 b <= n'가 됨

  n'까지만 검사하면 합성수를 이루는 a,b 중 작은 수까지 확인 가능함
  합성수가 존재하지 않으면 소수임
"""

m, n = map(int, input().split())

pri = [True for i in range(n+1)]

for i in range(2, int(n**0.5)+1):
    if pri[i] == True:
        j = 2
        while i*j <= n:
            pri[i*j] = False
            j += 1

for i in range(m, n+1):
    if i > 1:
        if pri[i]:
            print(i)
