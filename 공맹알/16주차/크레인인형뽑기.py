def solution(board, moves):
    answer = 0
    basket = []
    
    for move in moves:
        move-=1
        for i in range(len(board)):
            if board[i][move]!=0:
                if basket and basket[-1]==board[i][move]:
                    del basket[-1]
                    answer+=1
                    board[i][move]=0
                else:
                    basket.append(board[i][move])
                    board[i][move]=0
    return answer
