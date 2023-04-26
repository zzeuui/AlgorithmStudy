### 15-PUZZLE
- 양방향 탐색(bidirectional search)
   -  시작 정점에서 시작하는 정방향 탐색과 목표 정점에서 반대로 시작하는 역방향 탐색을 동시에 하며, 이 둘이 가운데서 만나면 탐색 종료
   -  유의사항   
      다음의 경우 사용하기 어려움
      - 역방향 간선 파악이 어려운 그래프
      - 각 정점마다 가능한 역방향 간선이 매우 많아, 역방향 탐색의 분기수가 큰 경우 
   -  구현
      - 정방향과 역방향 탐색에서 방문할 정점으로 모두 한 큐에 저장
      - 최단 거리를 저장할 때 정방향은 양수, 역방향은 음수로
      - 인접 정점의 상태 검사 결과 부호가 다르면 두 탐색이 만난 것
      ```
      class State;
      
      //부호 반환
      int sgn(int x) { if(!x) return 0; return x>0 ? 1 :-1; }
      //x의 절대값 1 증가
      int incr(int x) { if(x<0) return x-1; return x+1;
      
      int bidirectional(State start, State finish){
         map<State, int> c;
         queue<State> q;
         
         if(start == finish) return 0;
         
         //한 큐에 저장, 정방향은 양수 역방향은 음수
         q.push(start); c[start] = 1;
         q.push(finish); c[finish] = -1;
         
         while(!q.empty()){
            State here = q.front();
            q.pop();
            
            vector<State> adjacent = here.getAdjacent();
            for(int i = 0; i < adjacent.size(); ++i){
               map<State, int>::iterator it = c.find(adjacent[i]);
               if(it == c.end()){
                  c[adjacent[i]] == incr(c[here]);
                  q.push(adjacent[i]);
               }
               
               //인접정점(it)과 현재(here)의 부호가 다르다면 탐색 종료
               else if(sgn(it->second) != sgn(c[here]))
                  return abs(it->second) + abs(c[here]) -1;
            }
         }
         
         return -1
      }
      ```

- 점점 깊어지는 탐색(IDS, Iteratively Deepening Search)
   - 임의의 깊이 제한 $l$을 정한 후, 이 제한보다 짧은 목표 상태까지의 최단 경로가 존재하는지 DFS로 확인. 답을 찾지 못하면 $l$을 늘려서 다시 시도
   - 구현
   ```
   
   ```
