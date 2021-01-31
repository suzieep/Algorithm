n = int(input())
res = 0
board=[0]*15
def recursive(x):
    global res
    if x == n:
        res += 1
        return
    for i in range(n):
        board[x] = i
        if check(x):
            recursive(x+1)


def check(x):
    for i in range(x):
        if board[x] == board[i] or abs(board[i]-board[x]) == x-i:
            return False
    return True

recursive(0)
print(res)