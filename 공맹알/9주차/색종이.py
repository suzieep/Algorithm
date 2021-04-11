n = int(input())
a = 0

arr = [[0 for k in range(101)] for k in range(101)]
for k in range(n):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            arr[i][j] = 1
for x in arr:
    a += x.count(1)
print(a)