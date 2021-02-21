# DFS

```python

def dfs(graph, v, visited):
    visited[v]=True         # 현재 node visited 체크하기
    print(v, end=' ')       # 방문 위치 print
    for i in graph[v]:      # 그래프 연결된 위치에 대해서 방문되지 않은 곳 있으면 dfs 호출하기
        if not visited[i]:
            dfs(graph,i,visited)

graph = [[],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]

visited = [False]*9
dfs(graph,1,visited)

```
> DFS
> - 스택 사용
> - 재귀함수 사용
