#23:00 
#교재 풀이 보면서 정리
n,m = map(int,input().split())

board=[]
cnt = 0
for i in range(n):
    board.append(list(map(int,input())))

print (board)
def dfs(x,y):
    if x<=-1 or y<=-1 or x>=m or y>=n:
        return False
    if board[y][x]==0:
        print(x,y)
        board[y][x]=1
        dfs(x+1,y)
        dfs(x,y+1)
        dfs(x-1,y)
        dfs(x,y-1)
        return True
    return False

for y in range(n):
    for x in range(m):
        if dfs(x,y)==True:
            dfs(x,y)
            cnt+=1
            print ("count")

print(cnt)

#23:50