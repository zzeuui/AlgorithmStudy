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
   - BFS는 방문할 정점 목록을 저장해 메모리 사용량이 높지만, DFS는 발견 즉시 정점을 방문함
   - 효율성 평가
      - 메모리를 적게 사용하면서, 최단 거리보다 먼 정점들을 탐색하지 않음
      - 그러나 깊이 제한을 늘려 가며 DFS를 반복 수행하면 한 정점을 두 번 이상 방문하는 낭비 발생
   - 구현
   ```
   class State;
   int best;
   
   void dfs(State here, const State& finish, int steps){
      //지금까지 구한 최단 경로보다 더 좋을 가능성이 없으면 버림
      if(steps >= best) return;
      //목표 정점에 도달한 경우
      if(here == finish) { best = steps; return;}
      
      //dfs
      vector<State> adjacent = here.getAdjacent();
      for(int i = 0; i < adjacent.size(); ++i)
         dfs(adjacent[i], finish, steps+1);
   }   
   
   int ids(State start, State finish, int growthStep){
      for(int limit = 4; ; limit += growthStep){
         best = limit+1;
         dfs(start, finish, 0);
         if(best <= limit) return best;
      }
      return -1
   }
   ```
- 탐색 방법 선택
   - 상태 공간에서의 최단 경로를 찾는 경우, BFS를 우선적으로 고려
   - 탐색의 최대 깊이가 정해져있고, BFS를 수행하기에 메모리와 시간이 부족할 경우 양방향 탐색 고려
   - BFS와 양방향 탐색 모두 메모리를 많이 사용하거나 너무 느린 경우, IDS 고려 
