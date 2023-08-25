in_a = list(input())
in_b = list(input())

a = dict()
b = dict()
for i, s in enumerate(in_a):
    if s not in a:
        a[s] = i
for i, s in enumerate(in_b):
    if s not in b:
        b[s] = i

diff = 0
op_num = 0
for a_k, a_v in a.items():
    pre = a_v + diff
    if a_k in b:
        if pre < b[a_k]:
            diff += abs(a_v - b[a_k])
            op_num += diff
    else:
        op_num += 1

if op_num == 0 and abs(len(in_a) - len(in_b)) > 0:
    op_num += abs(len(in_a)-len(in_b))

print(op_num)

"""
- python list and dictionary
len(a): O(1)
a[key] : O(1)
key in a: O(1)


56분 (30분)
검증 
1. 교체
abc / bbc / 1
cat / cut / 1
abc / abb / 1

2. 삽입
abc / aabc, cabc / 1
abc / abbc, abec / 1
abc / abcc, abce / 1

3. 삭제
abc / bc, ac, ab / 1

4. 교체, 삽입, 삭제
unday / saturda / 5(in sat/ n->r/ re y)
"""

"""
책풀이

두 문자가 같은 경우: dp[i][j] = dp[i-1][j-1]
-> 왼쪽 위에 해당하는 수를 그대로 대입
두 문자가 다른 경우: dp[i][j] = 1+min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
-> 왼쪽(삽입), 위쪽(삭제), 왼쪽 위(교체)에 해당하는 수 중에서 가장 작은 수에 1을 더해 대입

이해가 안돼...
"""
def edit_dist(str1, str2):
    n = len(str1)
    m = len(str2)

    dp = [[0]*(m+1) for _ in range(n+1)]

    #거리 계산을 위해 글자의 위치로 초기화
    for i in range(1, n+1):
        dp[i][0] = i
    for j in range(1, m+1):
        dp[0][j] = j

    for i in range(1, n+1):
        for j in range(1, m+1):
            #지금까지 계산된 최소 편집 거리(표의 왼쪽 위)를 그대로 대입
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1+min(dp[i][j-1], #삽입(왼쪽): ???
                                 dp[i-1][j], #삭제(위쪽): ???
                                 dp[i-1][j-1])#교체(왼쪽 위): 지금까지 계산된 최소 편집 거리 + 1

