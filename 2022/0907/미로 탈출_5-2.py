#23:57
from collections import deque

n,m = map(int,input().split())
board=[]
length_arr =[]
dx = [1,0,-1,0]
dy = [0,1,0,-1]
for i in range(n):
    board.append(list(map(int,input().split())))
    length_arr.append([0 for _ in range(m)])

print(length_arr)
#hint bfs
#12:07

def bfs():
    q = deque()
    length = 0
    while q:
        print(1)

    return 0

