"""
오답
정확성 60.0
합계 60.0 / 100.0
"""
def solution(n, weak, dist):
    answer = float('inf')
    
    mid = int(n/2)
    odd = (n%2 != 0)
    
    num_weak = len(weak)
    
    for _ in range(num_weak):
        visited = [0]*n
        temp = start = weak.pop(0)
        visited[start] = 1
        cnt = 0
        for f in dist[::-1]:
            cnt += 1
            if sum(visited)+1 == num_weak:
                answer = min(answer, cnt)
                break
                
            for i, w in enumerate(weak):
                if visited[w] == 0:
                    f -= mid - abs(mid - abs(start-w))
                    
                    if odd and abs(start-w) > mid:
                        f -= 1
                        
                    if f >= 0:
                        visited[w] = 1
                        start = w
                        
                    if f <= 0:
                        start = weak[(i+1)%len(weak)]
                        break
                                        
            if sum(visited) == num_weak:
                answer = min(answer, cnt)
                break
                       
        weak.append(temp)
        
    if answer == float('inf'):
        return -1
    else:
        return answer
