arr = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

board = [0]*(max(arr)+1)  #0부터 최댓값까지 board에 넣기

for i in range(len(arr)):
    board[arr[i]]+=1

for i in range(len(board)):
    for j in range(board[i]):
        print(i,end=" ")