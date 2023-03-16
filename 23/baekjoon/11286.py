from sys import stdin
import heapq
from collections import defaultdict

if __name__=='__main__':
    heap = []
    flag = defaultdict(int)

    for _ in range(int(stdin.readline())):
        n = int(stdin.readline())
        flag[abs(n)]
        if n == 0:
            try:
                t = heapq.heappop(heap)
                if flag[t] > 0:
                    print(-t)
                    flag[t] -= 1
                else:
                    print(t)
            except:
                print(0)

        else:
            if n < 0:
                flag[abs(n)] += 1
            heapq.heappush(heap, abs(n))
        
