def solution(board, moves):
    answer = 0
    basket = [0]
    
    for move in moves:
        for i in range(len(board)):
            if board[i][move]!=0:
                if basket[-1]==board[i][move]:
                    del basket[-1]
                    answer+=1
                    board[i][move]=0
                else:
                    basket.append(board[i][move])
                    board[i][move]=0
    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

solution(board, moves)