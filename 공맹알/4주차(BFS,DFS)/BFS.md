# BFS

```python
from collections import deque   # deque import

def bfs(graph, start, visited):
    queue = deque([start])      # queue에 현재 위치 추가
    visited[start] = True       # 현재 위치 visited 체크

    while queue:                # queue가 비어있지 않는 동안
        v = queue.popleft()     # queue에서 처음을 빼서 v에 넣기
        print(v, end=' ')

        for i in graph[v]:      # v와 인접해있는 모든 node에 대해
            if not visited[i]:  # 아직 방문되어있지 않으면
                queue.append(i) # queue right에 쌓기
                visited[i]= True    #그리고 그 인접한 곳 모두 visited 체크해줌

graph = [[],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]

visited = [False]*9
bfs(graph,1,visited)
```
> BFS
> - 큐 사용 
> - ( 단 python의 경우 Queue말고 collections에서 deque 뽑아서 사용함)