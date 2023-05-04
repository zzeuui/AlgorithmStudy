import sys
import collections

input = sys.stdin.readline

def bellmanFord(g, src):
  upper = [float('inf')]*V
  upper[src] = 0
  updated = False
  
  for _ in range(V):
     #updated = False
     updated = list()
     for here in range(V):
        for there, cost in g[here]:
           if upper[there] > upper[here]+cost:
              upper[there] = upper[here]+cost
              #updated = True
              updated.append(there)
    
     if not updated: break 
  
  if updated: upper[0] = updated
  
  return upper


if __name__=='__main__':
    
    for _ in range(int(input())):
        V, w = map(int, input().rstrip().split())
        
        g1 = collections.defaultdict(list)
        g2 = collections.defaultdict(list)
        for _ in range(w):
            a, b, d = map(int, input().rstrip().split())
            g1[a].append([b, d])
            
            #최장경로를 구하기 위해 가중치의 부호를 반대로 설정
            g2[a].append([b, d*-1])

        cyc1, ret1 = bellmanFord(g1, 0)[0:2]
        if ret1 == float('inf'):
            print("UNREACHABLE")
        else:
            ret = ""
            if cyc1 == 0:
                ret = str(ret1) + " "
            else:
                ret = "INFINITY "
            cyc2, ret2 = bellmanFord(g2, 0)[0:2]
            if cyc2 == 0:
                ret += str(ret2*-1)
            else:
                ret += "INFINITY"
            
            print(ret)

