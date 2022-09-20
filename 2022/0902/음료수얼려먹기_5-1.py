#19:08
from collections import deque
n, m = map(int,input().split())
board = []
for i in range(n):
    tmp = list(map(str,input()))
    board.append(list(map(int, tmp)))

#19:12 BFS
dx=[1,0,-1,0]
dy=[0,1,0,-1]
def bfs (graph):
    queue = deque()
    count = 0
    for y in range(len(graph)):
        for x in range(len(graph[y])):
            if graph[y][x]==0:
                queue.append((y,x))
                graph[y][x]=1
                count+=1
                while queue:
                    v = queue.popleft()
                    print('v',v)
                    for i in range(4):
                        ny = v[0]+dy[i]
                        nx = v[1]+dx[i]
                        if ny>=0 and ny<len(graph) and nx>=0 and nx<len(graph[0]):
                            print(nx,ny)
                            node = graph[ny][nx]
                            if node ==0:
                                graph[ny][nx]=1
                                queue.append((ny,nx))
                                print ('queue',queue)
                    print(queue)
                    print(graph)
    print(count)    


graph_sample1=[[0,0,1,1,0],[0,0,0,1,1],[1,1,1,1,1],[0,0,0,0,0]]
graph_sample2=[[0000]]
bfs(board)

#19:59