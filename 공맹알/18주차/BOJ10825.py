n = int(input())

arr=[]
for i in range(n):
    arr.append(list(map(str,input().split())))
arr.sort(key=lambda arr: (-int(arr[1]), int(arr[2]), -int(arr[3]), arr[0]))
# sort를 lambda로 쉽게 할 수 있는 방법을 찾았다.
for i in range(n):
    print(arr[i][0]+" ")
