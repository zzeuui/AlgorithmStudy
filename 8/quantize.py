#책 그대로 했을 때, 시간 초과에 동적 계획법 적용도 못 함
#아래 다른 사람 정답 정리함
n = 0
cache = list()
A = list()
p_sum = list()
p_sq_sum = list()

def precalc():
    A.sort()
    p_sum.append(A[0])
    p_sq_sum.append(A[0]*A[0])
    for i in range(1, len(A)):
        p_sum.append(p_sum[i-1]+A[i])
        p_sq_sum.append(p_sq_sum[i-1]+A[i]*A[i])

def min_error(lo, hi):
    summ = p_sum[hi] - (0 if lo == 0 else p_sum[lo-1])
    sq_summ = p_sq_sum[hi] - (0 if lo == 0 else p_sq_sum[lo-1]) 
    m = int(0.5+summ/(hi-lo+1))

    ret = sq_summ - 2*m*summ + m*m*(hi-lo+1)

    return ret

def quantize(start, parts):

    if start == n: return 0
    if parts == 0: return 987654321
    ret = 987654321

    for i in range(1, n-start+1):
        ret = min(ret, min_error(start, start+i-1) +
                       quantize(start+i, parts-1))

    return ret

if __name__=='__main__':
    case_n = int(input())

    for _ in range(case_n):
        n_s = list(map(int, input().split(' ')))
        A = list(map(int, input().split(' ')))
        n, s = n_s[0], n_s[1]
        cache = [[-1]*(s+1)]*(n+1)
        precalc()
        ret = quantize(0, s)

        print(ret)

"""
#파이썬 가장 빠른 답
def d(i,j):
	#j-i가 1이라는 건 하나의 숫자에 대해서만 계산한다는 의미
	#자기자신 뿐이라 필연적으로 오차는 0
	if j - i == 1: return 0
	#i와 j의 모든 경우에 대해서 유니크한 숫자가 만들어짐. 
	#특정 구간을 레이블링하는 유니크한 숫자
	k = i * 100 + j
	#책과 동일한 논리
	#D[k] < 0일 때 i부터 j까지의 구간에 대해 계산한 적 없음
	if D[k] < 0:
		m = int(round((psum[j] - psum[i]) * 1. / (j-i)))
		D[k] = ppsum[j]-ppsum[i] - 2*m*(psum[j]-psum[i]) + m*m*(j-i)
	return D[k]

def f(i,s):
	#하나의 파트만 남았다면, 전달받은 구간의 시작(i)부터 끝(N)까지의 오차제곱을 구하면 됨
	if s == 1: return d(i,N) 
	#남은 숫자들이 하나씩 나눠지거나(필연적으로 오차는 0), 
	# 더이상 나눌 수 없을 때(이럴 때는 가장 큰 수를 넣어야 하는 거 아닌가?)
	if s+i >= N: return 0
	# i(from)과 s(part)의 모든 경우에 대해서 유니크한 숫자가 만들어짐 
	k = i * 10 + s 
	#책과 동일한 논리
	#F[k] < 0 일경우 i로 시작하고 s 파트일 때 계산한 적 없음 
	#현재 선택된 구간에 대한 오차제곱의 최소합 + 남은 구간, 남은 파트 수
	if F[k] < 0: F[k] = min(d(i,j) + f(j,s-1) for j in range(i+1,N))
	return F[k]

for _ in range(input()):
	N,s = map(int,raw_input().split())
	xs = sorted(map(int,raw_input().split()))
	psum, ppsum, prev, sprev = [0], [0], 0, 0
	for x in xs:
		prev += x
		sprev += x*x
		psum.append(prev)
		ppsum.append(sprev)
	F = [-1] * 1000
	D = [-1] * 10000
	print f(0,s)
"""