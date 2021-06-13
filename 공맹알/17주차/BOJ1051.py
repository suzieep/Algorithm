n, m = map(int, input().split())
board=[]
max_n = 0
for i in range(n):
    board.append(list(map(int,input())))

for y in range(n-1):
    for x in range(m-1):
        # x, y 둘 다 왼쪽 위 꼭짓점을 기준으로 찾아주면 되니까 1씩 빼준다.
        key = board[y][x]
        cnt = 1

        while cnt<min(n,m):
            # board 크기 숫자를 넘어가지 않도 cnt와 비교해 준다

            if y+cnt<n and x+cnt<m and board[y][x+cnt]==key and board[y+cnt][x]==key and board[y+cnt][x+cnt]==key:
                # cnt로 정사각형 크기 알 수 있게 해주고 max에 그에 따른 크기 저장
                max_n = max((cnt+1)**2,max_n)
            cnt+=1



print(max_n)