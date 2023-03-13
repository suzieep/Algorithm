n = int(input())
board =[]
for i in range(n):
    name, score = input().split()
    board.append((name, score))

arr = sorted(board, key=lambda student: student[1])

for i in arr:
    print(i[0],end=' ')