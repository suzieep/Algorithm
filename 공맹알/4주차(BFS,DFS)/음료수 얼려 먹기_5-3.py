n, m = map(int,input().split())

board = []
for i in range(n):
    tmp = list(map(str,input()))
    board.append(list(map(int, tmp)))
visited = board

f = []
cnt =0

dx = [0,1,0,-1] #북쪽부터 시계방향
dy = [-1,0,1,0]

def dfs(iy,ix):
    global visited,f
    
    visited[iy][ix] = 1
    f.append((iy,ix))

    count=0
    for i in range(len(dx)):
        tx = ix+dx[i]
        ty = iy+dy[i]
        count+=1
        if ty>=0 and ty<n and tx>=0 and tx<m:
            if visited[ty][tx] == 0:
                dfs(ty,tx)

    if count==4:
        if f:
            f.pop()
            if not f:
                return
            dfs(f[-1][0],f.pop()[1])
        else:
            return         

for i in visited:
    for j in i:
        if j==0:
            dfs(visited.index(i),i.index(j))
            cnt+=1

print(cnt)