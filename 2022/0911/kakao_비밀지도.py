# Lv1
# 38m
def solution(n, arr1, arr2):
    answer=[]
    board = [[" " for _ in range(n)] for _ in range(n)]
    arr1_board = []
    arr2_board = []
    for i in arr1:
        arr1_board.append(to_binary(n,i))
    for i in arr2:
        arr2_board.append(to_binary(n,i))
    
    for i in range(n):
        for j in range(n):
            if arr1_board[i][j] or arr2_board[i][j]:
                board[i][j]='#'
            else:
                board[i][j]=' '
        answer.append("".join(board[i]))
    return answer


def to_binary(n,input_ten):
    n_binary=[False]*n
    
    for i in range(n):
        tmp=2**(n-1-i)
        if input_ten>=tmp:
            input_ten-=tmp
            n_binary[i]=True
    return n_binary

            
        