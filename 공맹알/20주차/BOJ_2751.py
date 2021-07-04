# 간단하게 정렬을 진행해주면 된다.

n = int(input())
arr =[]
for i in range(n):
    arr.append(int(input()))
arr.sort()
for i in arr:
    print(i)