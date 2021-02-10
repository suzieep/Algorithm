dot = list(input())

x = ord(dot[0])-96
y = int(dot[1])
cnt = 0

dx = [-1,1,2,2,1,-1,-2,-2]
dy = [2,2,1,-1,-2,-2,-1,1]
for i in range(len(dx)):
    nx = x+dx[i]
    ny = y+dy[i]
    if nx<=8 and nx>=1 and ny>=1 and ny<=8:
        cnt+=1

print(cnt)