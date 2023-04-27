import sys
import collections
import heapq

input = sys.stdin.readline

INF = 1e9

if __name__=='__main__':
    for _ in range(int(input())):
        m = int(input())
        
        a_time = [0]*(m)
        m_diff = [0]*(m)

        for i in range(m):
            a, b = map(int, input().split())
            a_time[i] = a
            m_diff[i] = a-b

        time = collections.defaultdict(lambda: INF)
        
        q = list()

        for std_time, diff in zip(a_time, m_diff):
            heapq.heappush(q, (std_time, diff))

        while q:
            t, here = heapq.heappop(q)

            if time[here] < t:
                continue

            for std_time, diff in zip(a_time, m_diff):
                nt_time = t + std_time
                nt_node = here + diff

                if abs(nt_node) >= 200:
                    continue

                if time[nt_node] > nt_time:
                    time[nt_node] = nt_time
                    heapq.heappush(q, (nt_time, nt_node))

        print("IMPOSSIBLE" if time[0] == INF else time[0])

