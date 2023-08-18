n, c = list(map(int, input().split()))
array = []
for _ in range(n):
    array.append(int(input()))
array.sort()

start = 1 # 가능한 최소 거리(min gap)
end = array[-1] - array[0] # 가능한 최대 거리(max gap)
ret = 0

while(start <= end):
    mid = (start+end)//2 #mid는 가장 인접한 두 공유기 사이의 거리/2(gap)을 의미
    value = array[0]
    cnt = 1
    for i in range(1, n): # 앞에서부터 설치
        if array[i] >= value+mid: 
            value = array[i]
            cnt += 1
    if cnt >= c: # 공유기를 설치하면,
        start = mid+1 # 앞에서부터 gap(거리/2, 왼쪽)까지는 탐색했으니깐, 시작점을 증가
        ret = mid # 수행되면서 최대 gap은 계속 감소함
    else:
        end = mid-1 #공유기를 설치할 수 없으면, gap을 감소해서 더 왼쪽을 탐색

print(ret)
