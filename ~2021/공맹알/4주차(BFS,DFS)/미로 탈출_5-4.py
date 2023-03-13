from collections import deque

n,m = map(int,input().split())
board =[]
dx = [0,1,0,-1]
dy = [-1,0,+1,0]

for i in range(n):
    board.append(list(map(int,input())))
visited = board
def bfs(y,x):
    cnt = 1
    global visited, board
    visited[y][x]= 0
    q = deque()
    q.append((y,x))

    while 1:
        (y,x) = q.popleft()
        cnt+=1
        count=0
        for j in range(4):
            tx = x + dx[j]
            ty = y + dy[j]
            if tx>=0 and tx<m and ty>=0 and ty<n and visited[ty][tx]==1:
                if ty == n-1 and tx == m-1:
                    return cnt
                visited[ty][tx] = 0
                q.append((ty,tx))
                count+=1
        if count==0:
            cnt-=1
                
print(bfs(0,0))